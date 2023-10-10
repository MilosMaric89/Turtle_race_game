from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet: ", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() >= 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have win!")
            else:
                print("You have lost.")

        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)


















# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#
#     for turtle in all_turtles:
#         if turtle.xcor() >= 220:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You have won! The {winning_color} turtle is the winner.")
#             else:
#                 print(f"You have lost! The {winning_color} turtle is the winner.")
#         random_distance = random.randint(1, 10)
#         turtle.forward((random_distance))


screen.exitonclick()