from turtle import Turtle, Screen
import random

names = ["Nga", "Gia", "Oliver", "Oakley", "Xinh", "Loi"]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
xMax = 250
yMax = 300
screen.setworldcoordinates(-xMax, -yMax, xMax, yMax)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
turtle_ycor = 50
gif_images = ["Nga-red.gif", "Gia-orange.gif", "Oliu-yellow.gif", "Oak-green.gif",
              "Xinh-blue.gif", "Loi-purple.gif"]

for image in gif_images:
    screen.register_shape(image)

turtles = []
for i in range(len(names)):
    names[i] = Turtle(gif_images[i])
    names[i].penup()
    names[i].color(colors[i])
    turtle_xcor = -xMax + 10
    turtle_ycor += ((-1) ** i) * i * 100
    names[i].goto(turtle_xcor, turtle_ycor)
    turtles.append(names[i])


def game_start():
    global user_bet
    # print(user_bet)
    racing_mode = True
    for turtle in turtles:
        turtle.setx(-xMax + 10)

    while racing_mode:
        for turtle in turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() >= xMax:
                winning_color = turtle.color()
                # print(winning_color)
                if user_bet == winning_color:
                    user_reply = str(screen.textinput(title="Congrats! You win!",
                                                  prompt="Do you want to bet again? Pick a color: "))
                    if user_reply.lower() in colors:
                        user_bet = user_reply.lower()
                        game_start()
                    else:
                        racing_mode = False
                else:
                    user_reply = str(screen.textinput(title="Sorry, you lose!",
                                                prompt="Do you want to bet again? Pick a color: "))
                    if user_reply.lower() in colors:
                        user_bet = user_reply.lower()
                        game_start()
                    else:
                        racing_mode = False


screen.listen()
screen.onkey(key="space", fun=game_start)
screen.exitonclick()
