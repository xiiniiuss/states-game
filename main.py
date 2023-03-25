from turtle import Turtle, Screen

screen = Screen()
screen.title('US States Quiz')
screen.bgcolor('black')

IMAGE = 'blank_states_img.gif'
screen.addshape(IMAGE)

photo = Turtle()
photo.shape(IMAGE) 

thing = Turtle()
thing.hideturtle()
thing.penup()

import pandas as pd

data = pd.read_csv("states.csv")
data_dict = data.to_dict()

states_list = data.state.to_list()

states_number = 50
score = 0

while states_number > 0:
    user_answer = screen.textinput(title=f"Correct answers : {score} ", prompt="Enter another state's name :").title()
    if user_answer in states_list:
        i = states_list.index(user_answer)
        x_pos = data_dict['x'][i]
        y_pos = data_dict['y'][i]
        thing.goto(x=x_pos, y=y_pos)
        thing.write(user_answer)
        score += 1
        states_number -= 1
    elif user_answer == 'Exit' :
        states_number = 0
        



screen.exitonclick()

