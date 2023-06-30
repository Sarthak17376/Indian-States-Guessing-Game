from turtle import Turtle, Screen
import pandas

screen = Screen()
name_turtle = Turtle()
name_turtle.hideturtle()
name_turtle.up()
screen.setup(width=600, height=600)
screen.title("Name of States")
screen.bgpic('India.gif')

data = pandas.read_csv("states_data.csv")

states_dict = {}
guessed_states = []
missing_states = []
for (state_name, x_cor, y_cor) in zip(data.Name.to_list(), data.x.to_list(), data.y.to_list()):
    states_dict[state_name] = (int(x_cor), int(y_cor))

while len(guessed_states) < 29:
    guess = screen.textinput("Guess a State!!!", prompt="Input Here").upper()
    print(guess)
    if guess in states_dict:
        name_turtle.goto(states_dict[guess])
        guessed_states.append(guess)
        name_turtle.write(guess)
    elif guess == "EXIT":
        for states in states_dict:
            if states not in guessed_states:
                missing_states.append(states)
        new_learning_data = pandas.DataFrame(missing_states)
        new_learning_data.to_csv("learn_states.cvs")
        break

if len(guessed_states) == 29:
    name_turtle.clear()
    name_turtle.goto(0,0)
    name_turtle.write("CONGRATULATIONS!!!!", font=30)
    screen.exitonclick()

