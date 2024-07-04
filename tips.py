import os
import customtkinter as ctk


def generate():
    prompt = "Please give me the important tips for a person who"

    gender = gender_dropdown.get()
    prompt += "is" + gender +"."

    age = age_dropdown.get()
    prompt += "And also age is between" + age

    about = tags_dropdown.get()
    prompt += "about" + about

    import openai

    # Set up your API key
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print(response.choices[0].message.content)



tips = ctk.CTk()
tips.geometry('750x550')
tips.title("Health Tips")
ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(tips,text="Health Tips",font=ctk.CTkFont(size=30,weight="bold"))
title_label.pack(padx = 10,pady =(40,20))

frame = ctk.CTkFrame(tips)
frame.pack(fill="x",padx=100)

gender = ctk.CTkFrame(frame)
gender.pack(padx=100,pady=(20,5),fill="both")
gender_label = ctk.CTkLabel(gender,text="Gender ",font=ctk.CTkFont(weight="bold"))
gender_label.pack()
gender_dropdown = ctk.CTkComboBox(gender,values=['Male','Female','Others'])
gender_dropdown.pack(pady=10)

age = ctk.CTkFrame(frame)
age.pack(padx=100,pady=(20,5),fill="both")
age_label = ctk.CTkLabel(age,text="Age ",font=ctk.CTkFont(weight="bold"))
age_label.pack()
age_dropdown = ctk.CTkComboBox(age,values=['below 19','20-39','40-59',"60+"])
age_dropdown.pack(pady=10)


tags = ctk.CTkFrame(frame)
tags.pack(padx=100, pady=(20, 5), fill="both")
tags_label = ctk.CTkLabel(tags, text="Health tips for", font=ctk.CTkFont(weight="bold"))
tags_label.pack()
tags_dropdown = ctk.CTkComboBox(tags, values=[
    "Allergies and Asthma Management",
    "Art Therapy for Stress Relief",
    "Barre Workouts for Flexibility",
    "Bone and Joint Health",
    "Cancer Prevention and Awareness",
    "Child Health and Development",
    "Cognitive Behavioral Therapy (CBT) Techniques",
    "CrossFit Training Tips",
    "DIY Home Workouts",
    "Diabetes Care and Prevention",
    "Digestive Health",
    "Emergency Preparedness",
    "Ergonomics and Posture",
    "Eye Health",
    "Gardening for Physical Activity",
    "Gut Health and Probiotics",
    "Healthy Aging",
    "Healthy Habits and Lifestyle Changes",
    "Heart Health",
    "High-Intensity Interval Training (HIIT)",
    "Holistic Health Approaches",
    "Hydration and Water Intake",
    "Immune System Boosting",
    "Interval Training Workouts",
    "Journaling for Mental Clarity",
    "Managing Chronic Conditions",
    "Mediterranean Diet Benefits",
    "Mental Health and Well-being",
    "Men's Health",
    "Mindful Eating Practices",
    "Music Therapy for Relaxation",
    "Nutrition and Diet",
    "Oral Health",
    "Pain Management",
    "Pets and Mental Health Benefits",
    "Physical Activity and Exercise",
    "Pilates for Core Strength",
    "Plant-Based Nutrition",
    "Positive Psychology Practices",
    "Preventive Health Care",
    "Seasonal Health Tips",
    "Self-Care Practices",
    "Skin Health",
    "Social Health and Relationships",
    "Special Populations",
    "Travel Health",
    "Women's Health",
    "Work-Life Balance",
    "Yoga and Mindfulness Practices"
])
tags_dropdown.pack(pady=10)

button = ctk.CTkButton(frame,text="Generate Tips",command=generate)
button.pack(padx=100,fill="x",pady=(5,20))

result = ctk.CTkTextbox(tips,font=ctk.CTkFont(size=15))
result.pack(pady=10,fill="x",padx=100)

tips.mainloop()

