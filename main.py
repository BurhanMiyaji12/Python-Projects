import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

score = 0
while len(guessed_states) < 50:

    answer_states = screen.textinput(title= f"{score}/50 States Correct", prompt="What are the states?").title()

    if answer_states == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_states in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_states)
        guessed_states.append(answer_states)
        score += 1



# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()