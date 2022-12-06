import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
guessed_states = []

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name?").capitalize()
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
