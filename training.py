import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.optimizers import SGD
import random
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# Initialize WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Initialize NLTK's VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Read intents from JSON file
with open('intents.json') as json_file:
    intents = json.load(json_file)

# Initialize lists for words, classes, and documents
words = []
classes = []
documents = []
ignore_words = ['?', '!']

# Iterate through intents and their patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize words
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # Add documents to the corpus
        documents.append((w, intent['tag']))
        # Add to classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize, lowercase each word, and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Print some information about the data
print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "unique lemmatized words", words)

# Save words and classes to pickle files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Create training data
training = []

# Create an empty array for the output
output_empty = [0] * len(classes)

# Create training set: bag of words for each sentence
for doc in documents:
    # Initialize bag of words
    bag = []
    # List of tokenized words for the pattern
    pattern_words = doc[0]
    # Lemmatize each word and create base word to represent related words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # Create bag of words array with 1 if word match found in current pattern
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    # Output is '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# Shuffle training data
random.shuffle(training)

# Convert training data to NumPy array
X_train = np.array([entry[0] for entry in training])
y_train = np.array([entry[1] for entry in training])

print("Training data created")

# Define input shape
input_shape = (len(X_train[0]),)

# Define Input layer
inputs = Input(shape=input_shape)

# Add Dense layers and Dropout layers
x = Dense(128, activation='relu')(inputs)
x = Dropout(0.5)(x)
x = Dense(64, activation='relu')(x)
x = Dropout(0.5)(x)
outputs = Dense(len(y_train[0]), activation='softmax')(x)

# Create model
model = Model(inputs=inputs, outputs=outputs)

# Compile model
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fit model
hist = model.fit(X_train, y_train, epochs=100, batch_size=5, verbose=1)

import matplotlib.pyplot as plt


# Plot training history
def plot_training_history(history):
    plt.figure(figsize=(10, 5))

    # Plot accuracy
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'])
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend(['Train'], loc='upper left')

    # Plot loss
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'])
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend(['Train'], loc='upper left')

    plt.tight_layout()
    plt.show()

# Print accuracy and loss from training history
print("Accuracy:", hist.history['accuracy'])
print("Loss:", hist.history['loss'])

# Plot training history
plot_training_history(hist)


# Save model
model.save('chatbot_model.h5', hist)
print("Model created and saved")

# Function to determine sentiment of a sentence
def analyze_sentiment(sentence):
    # Get sentiment scores
    scores = sid.polarity_scores(sentence)
    # Determine sentiment label based on compound score
    if scores['compound'] >= 0.05:
        return 'positive'
    elif scores['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Function to predict intent and respond
def chatbot_response(text):
    # Preprocess user input
    sentence_words = nltk.word_tokenize(text)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    # Generate bag of words
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    # Predict intent
    results = model.predict(np.array([bag]))[0]
    # Get index of highest probability
    index = np.argmax(results)
    # Get corresponding tag
    tag = classes[index]
    # Filter intents for matching tag
    intent = [intent for intent in intents['intents'] if intent['tag'] == tag][0]
    # Get list of responses
    responses = intent['responses']
    # Choose a random response
    response = random.choice(responses)
    # Analyze sentiment of response
    sentiment = analyze_sentiment(response)
    return response, sentiment

# Example usage:
# user_input = "What are the symptoms of COVID-19?"
# response, sentiment = chatbot_response(user_input)
# print("Bot Response:", response)
# print("Sentiment:", sentiment)
