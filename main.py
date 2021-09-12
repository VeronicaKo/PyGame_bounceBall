# https://youtu.be/nGDCPL5TE2Y
# Прыгающий мячик Bounce ball | Программирование на Python

import turtle, random

window = turtle.Screen()
border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.color('violet')
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)

balls = []
count = 10
for i in range(count):
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.shape('turtle')
    red =random.random()
    green =random.random()
    blue =random.random()
    ball.color(red,green,blue)
    ball.up()
    randx = random.randint(-290, 290)
    randy = random.randint(-290, 290)
    ball.goto(randx, randy)
    ball.showturtle()
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    balls.append([ball, dx, dy])

while True:
    for i in range(count):
        balls[i]
        x, y = balls[i][0].position()
        if x + balls[i][1] >= 290 or x + balls[i][1] <= -290:
            balls[i][1] = -balls[i][1]
        if y + balls[i][2] >= 290 or y + balls[i][2] <= -290:
            balls[i][2] = -balls[i][2]
        try:
            balls[i][0].goto(x + balls[i][1], y + balls[i][2])
        except:
            exit()

window.mainloop()
