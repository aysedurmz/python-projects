import turtle
import random

#screen setup
screen = turtle.Screen()
screen.bgcolor("CadetBlue2")
screen.title("Catch the Turtle")

# Turtle setup
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color("green", "green")
myTurtle.penup()

# Timer turtle
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
height = screen.window_height() /2 *0.8
timer_turtle.goto(0, height)

# Score turtle
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.pencolor("DarkBlue")
height = screen.window_height() /2 *0.9
score_turtle.goto(0, height)

timer = 15
score = 0
score_turtle.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

def score_function(x, y):
    if timer > 0:
        global score
        score_turtle.clear()
        score += 1
        score_turtle.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

def teleport_turtle():
    if timer > 0:
        x = random.randint(-350, 350)
        y = random.randint(-340, 270)
        myTurtle.goto(x, y)

def timer_function():
    global timer
    timer_turtle.clear()
    if timer == 0:
        timer_turtle.write("Game Over!", align="center", font=("Arial", 16, "bold"))
    else:
        timer_turtle.write(f"Time: {timer}" , align="center", font=("Arial", 16, "bold"))
        teleport_turtle()
        timer -= 1
        screen.ontimer(timer_function, 1000)


# Start
myTurtle.onclick(score_function)
timer_function()
turtle.mainloop()