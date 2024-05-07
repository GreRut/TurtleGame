from turtle import Turtle, Screen
from random import randint

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win the race? Pick a colour:")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = -70
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions)
    y_positions += 30
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You have won! The winning turtle is {winning_turtle}")
            else:
                print("Unfortunately, you have lost.")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
