import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
col = ("yellow", "pink", "cyan", "light green", "red")

for i in range(150):
    t.pencolor(col[i%4])
    t.circle(190 - i / 2, 90)
    t.lt(90)
    t.circle(190 - i / 3, 90)
    t.lt(60)
s.exitonclick()