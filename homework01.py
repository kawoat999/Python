import turtle

turtle.width(5)
turtle.forward(1)
turtle.color("black")

turtle.fillcolor("red")
turtle.begin_fill()

turtle.circle(30)
turtle.penup()
turtle.forward(60)
turtle.pendown()
turtle.circle(30)
turtle.penup()
turtle.forward(60)
turtle.pendown()
turtle.circle(30)

turtle.end_fill()

turtle.color("black")

turtle.fillcolor("blue")
turtle.begin_fill()


turtle.left(-110)
turtle.forward(200)
turtle.right(145)
turtle.forward(200)
turtle.right(105)
turtle.forward(120)
turtle.left(180)
turtle.forward(120)
turtle.right(90)

turtle.end_fill()

turtle.penup()
turtle.right(-5)
turtle.forward(60)
turtle.pendown()

turtle.fillcolor("green")
turtle.begin_fill()

turtle.color("green")
turtle.circle(-70,190)
turtle.right(175)
turtle.circle(10,180)
turtle.right(180)
turtle.circle(10,180)
turtle.right(180)
turtle.circle(10,180)
turtle.right(180)
turtle.circle(10,180)
turtle.right(180)
turtle.circle(10,180)
turtle.right(180)
turtle.circle(10,180)
turtle.right(180)
turtle.circle(10,180)

turtle.end_fill()

turtle.penup()
turtle.left(180)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)

turtle.color("red")
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(-20)
turtle.end_fill()
turtle.penup()

turtle.right(90)
turtle.forward(20)
turtle.left(140)
turtle.forward(10)
turtle.color("black")
turtle.pendown()
turtle.forward(30)


turtle.mainloop()