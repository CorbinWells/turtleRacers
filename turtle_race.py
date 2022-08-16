import random
from turtle import Turtle, Screen
import turtle
my_screen = Screen()
screen_width = 400
screen_height = 300
my_screen.setup(980, 600)
my_screen.screensize(canvwidth=screen_width, canvheight=screen_height)
colors = ["green", "blue", "red", "purple", "yellow"]
x_position = screen_width / screen_width - screen_width
y_position = [-200, -100, 0, 100, 200]
turtle_racers = []
turtle.title("Turtle Race")
my_screen.bgcolor("peru")

# finish line
size = 20
turtle.shape("square")
turtle.penup()
# black part
turtle.color("black")
for b in range(12):
    turtle.goto(400, (250 - (b * size * 2 + 20)))
    turtle.stamp()
#white part
turtle.color("white")
for w in range(12, -1, -1):
    turtle.goto(400, (250 - (w * size * 2)))
    turtle.stamp()

for racers in range(0, 5):
    new_racer = Turtle(shape="turtle")
    new_racer.color(colors[racers])
    new_racer.penup()
    new_racer.goto(x=x_position, y=y_position[racers])
    turtle_racers.append(new_racer)

bet = my_screen.textinput(title="What color will win", prompt="[green] [blue] [red] [purple] [yellow]")
if bet:
    start_race = True
else:
    print("No bet made game over")

# for leaderboard below
positions = []
positions_color = []
places = ["5th", "4th", "3rd", "2nd"]

while start_race == True:
    for racers in turtle_racers:
        positions.append(racers.xcor())
        positions_color.append(racers.pencolor())
        if racers.xcor() > screen_width - 12:
            start_race = False
            winner = racers.pencolor()
            # for leaderboard positions
            position = positions[-5:]
            colors = positions_color[-5:]
            zipped = zip(position, colors)
            pairs = sorted(zipped)
            tuples = zip(*pairs)
            position, colors = [list(tuple) for tuple in tuples]
            board = Turtle()
            board.penup()
            board.hideturtle()
            for b in range(len(colors)-2, -1, -1):
                board.goto(-135, (-160 - (-b * -size * -2)))
                board.color(colors[b])
                board.write(f"{places[b]} {colors[b]}", font=("Arial", 18, "normal"))
            if winner == bet:
                text = Turtle()
                text.hideturtle()
                text.color(winner)
                text.write(f"{winner} wins, you win", align="Center", font=("Arial", 24, "normal"))
            else:
                text = Turtle()
                text.hideturtle()
                text.color(winner)
                text.write(f"{winner} wins, you lose", align="Center", font=("Arial", 24, "normal"))
        random_steps = random.randint(0, 20)
        racers.forward(random_steps)
my_screen.exitonclick()
