from tkinter import *

window = Tk()
window.geometry("400x200")
window.title("BMI Calculator")
window.configure(bg="light pink")

#Labels
weight_label = Label(text="Enter Your Weight (kg)", bg="light salmon")
weight_label.place(relx=0.5, rely=0.2, anchor="center")
height_label = Label(text="Enter Your Height (cm)", bg="light salmon")
height_label.place(relx=0.5, rely=0.45, anchor="center")

last_label = Label(bg="light pink")
last_label.place(relx=0.5, rely=0.85, anchor="center")

#Entries
weight_entry = Entry(width=15)
weight_entry.place(relx=0.5, rely=0.3, anchor="center")
height_entry = Entry(width=15)
height_entry.place(relx=0.5, rely=0.55, anchor="center")

def calculate_bmi(weight, height):
    if height == 0:
        last_label.config(text="Please enter a valid height.")
    else:
        meter = height / 100
        bmi = weight / pow(meter, 2)
        if bmi < 18.5:
            result = "underweight"
        elif 18.5 <= bmi < 25:
            result = "normal weight"
        elif 25 <= bmi < 30:
            result = "overweight"
        elif bmi >= 30:
            result = "obese weight"
        else:
            result = "invalid option"
        last_label.config(text=f"Your BMI is: {bmi:.1f}. You are {result}")

def get_input():
    str_weight = weight_entry.get()
    str_height = height_entry.get()
    if str_weight == "" or str_height == "":
        last_label.config(text="Enter both weight and height")
    else:
        try:
            weight = float(str_weight)
            height = float(str_height)
            calculate_bmi(weight, height)
        except ValueError:
            last_label.config(text="Enter a valid number!")

#Button
calculate_button = Button(text="Calculate", width=10, command=get_input)
calculate_button.place(relx=0.5, rely=0.7, anchor="center")

mainloop()