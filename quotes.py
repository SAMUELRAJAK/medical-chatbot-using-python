import tkinter as tk
from tkinter import messagebox
import random

class TipGeneratorApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Healthcare quotes")
        self.master.geometry("1300x700")  # Set the window size
        self.master.resizable(0,0)  # Make the window non-resizable

        # Background image
        self.background_image = tk.PhotoImage(file="images/quotes.png")
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.tip_text = tk.Text(master, height=15, width=40, font=("Arial", 18,"italic"), bg="#FFF6E9", bd=0)
        self.tip_text.place(x=370,y=130)

        self.generate_button = tk.Button(master, text="Generate Tip", font=("Arial", 16), command=self.generate_tip)
        self.generate_button.place(x=370,y=380)

        def home():
            master.destroy()
            import dashboard

        self.quit_button = tk.Button(master, text="Home", font=("Arial", 16), command=home)
        self.quit_button.place(x=800,y=380)

    def generate_tip(self):
        health_tips = [
            "Take care of your body. It's the only place you have to live. - Jim Rohn",
            "Health is a state of complete harmony of the body, mind, and spirit. - B.K.S. Iyengar",
            "The greatest wealth is health. - Virgil",
            "Good health is not something we can buy. However, it can be an extremely valuable savings account. - Anne Wilson Schaef",
            "The first wealth is health. - Ralph Waldo Emerson",
            "To ensure good health: eat lightly, breathe deeply, live moderately, cultivate cheerfulness, and maintain an interest in life. - William Londen",
            "An apple a day keeps the doctor away.",
            "Your body hears everything your mind says.",
            "The doctor of the future will no longer treat the human frame with drugs, but rather will cure and prevent disease with nutrition. - Thomas Edison",
            "The mind and body are not separate. What affects one, affects the other.",
            "Happiness is the highest form of health.",
            "Health is not simply the absence of sickness. - Hannah Green",
            "A healthy outside starts from the inside. - Robert Urich",
            "Those who think they have no time for healthy eating will sooner or later have to find time for illness. - Edward Stanley",
            "Let food be thy medicine and medicine be thy food. - Hippocrates",
            "The groundwork of all happiness is health. - Leigh Hunt",
            "The greatest wealth is health. - Virgil",
            "Health is like money, we never have a true idea of its value until we lose it. - Josh Billings",
            "Physical fitness is not only one of the most important keys to a healthy body, it is the basis of dynamic and creative intellectual activity. - John F. Kennedy",
            "The doctor of the future will give no medicine, but will instruct his patients in care of the human frame, in diet, and in the cause and prevention of disease. - Thomas Edison",
            "The greatest wealth is health.,Virgil",
            "Let food be thy medicine and medicine be thy food.,Hippocrates",
            "Health is a state of complete harmony of the body, mind, and spirit.,B.K.S. Iyengar",
            "The first wealth is health.,Ralph Waldo Emerson",
            "To keep the body in good health is a duty... otherwise we shall not be able to keep our mind strong and clear.,Buddha",
            "Time and health are two precious assets that we don't recognize and appreciate until they have been depleted.,Denis Waitley",
            "A good laugh and a long sleep are the best cures in the doctor's book.,Irish Proverb",
            "The only way to keep your health is to eat what you don't want, drink what you don't like, and do what you'd rather not.,Mark Twain",
            "Health is not valued till sickness comes.,Thomas Fuller",
            "Your body hears everything your mind says.,Naomi Judd",
            "Health is like money, we never have a true idea of its value until we lose it.,Josh Billings",
            "The best doctor gives the least medicines.,Benjamin Franklin",
            "The wish for healing has always been half of health.,Lucius Annaeus Seneca",
            "Take care of your body. It's the only place you have to live.,Jim Rohn",
            "Happiness is nothing more than good health and a bad memory.,Albert Schweitzer",
            "An apple a day keeps the doctor away.,Proverb",
            "It is health that is real wealth and not pieces of gold and silver.,Mahatma Gandhi",
            "He who has health has hope, and he who has hope has everything.,Arabian Proverb",
            "Healthy citizens are the greatest asset any country can have.,Winston S. Churchill",
            "Health is the soul that animates all the enjoyments of life, which fade and are tasteless without it.,Seneca",
            "Health is the thing that makes you feel that now is the best time of the year.,Franklin P. Adams",
            "The greatest of follies is to sacrifice health for any other kind of happiness.,Arthur Schopenhauer",
            "To get rich never risk your health. For it is the truth that health is the wealth of wealth.,Richard Baker",
            "The groundwork for all happiness is good health.,Leigh Hunt",
            "Take care of your body. It's the only place you have to live.,Jim Rohn",
            "Health is not a condition of matter, but of mind.,Mary Baker Eddy",
            "The human body has been designed to resist an infinite number of changes and attacks brought about by its environment. The secret of good health lies in successful adjustment to changing stresses on the body.,Harry J. Johnson",
            "The more you eat, the less flavor; the less you eat, the more flavor.,Chinese Proverb",
            "A healthy attitude is contagious but don't wait to catch it from others. Be a carrier.,Tom Stoppard",
            "A healthy outside starts from the inside.,Robert Urich",
            "Healthy citizens are the greatest asset any country can have.,Winston S. Churchill",
            "A man too busy to take care of his health is like a mechanic too busy to take care of his tools.,Spanish Proverb",
            "The greatest wealth is health.,",
            "Those who do not find time for exercise will have to find time for illness.,Earl of Derby",
            "The only way to keep your health is to eat what you don't want, drink what you don't like, and do what you'd rather not.,Mark Twain",
            "Physical fitness is not only one of the most important keys to a healthy body, it is the basis of dynamic and creative intellectual activity.,John F. Kennedy",
            "A fit, healthy body—that is the best fashion statement.,Jess C. Scott",
            "When diet is wrong, medicine is of no use. When diet is correct, medicine is of no need.,Ayurvedic Proverb",
            "Health is the greatest possession. Contentment is the greatest treasure. Confidence is the greatest friend.,Lao Tzu",
            "It's never too early or too late to work towards being the healthiest you.,",
            "The doctor of the future will no longer treat the human frame with drugs, but rather will cure and prevent disease with nutrition.,Thomas Edison",
            "Your health is what you make of it. Everything you do and think either adds to the vitality, energy and spirit you possess or takes away from it.,Ann Wigmore",
            "The part can never be well unless the whole is well.,Plato",
            "Prevention is better than cure.,Desiderius Erasmus",
            "He who takes medicine and neglects to diet wastes the skill of his doctors.,Chinese Proverb",
            "A merry heart doeth good like a medicine, but a broken spirit dries the bones.,Proverbs 17:22",
            "The doctor of the future will give no medicine but will instruct his patient in the care of the human frame, in diet and in the cause and prevention of disease.,Thomas Edison",
            "Our bodies are our gardens – our wills are our gardeners.,William Shakespeare",
            "Sickness comes on horseback but departs on foot.,Dutch Proverb",
            "The art of medicine consists of amusing the patient while nature cures the disease.,Voltaire",
            "True healthcare reform starts in your kitchen, not in Washington.,",
            "Health is not just about what you're eating. It's also about what you're thinking and saying.,",
            "Our bodies are our temples; keeping them clean is essential to our well-being.,"

        ]
        tip = random.choice(health_tips)
        self.tip_text.delete('1.0', tk.END)
        self.tip_text.insert(tk.END, tip)



def main():
    root = tk.Tk()
    app = TipGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
