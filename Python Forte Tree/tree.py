import random
import turtle

def tree(size, myTurtle):
	myTurtle.pensize(size / 20)

	if size < random.randint(2, 3) * 20:
		myTurtle.color("green")
	else:
		myTurtle.color("blue")

	if size > 5: 
		myTurtle.forward(size)
		myTurtle.left(25)
		tree(size - random.randint(10, 20), myTurtle)
		myTurtle.right(50)
		tree(size - random.randint(10, 20), myTurtle)
		myTurtle.left(25)
		myTurtle.penup()
		myTurtle.backward(size)
		myTurtle.pendown()


window = turtle.Screen()
window.bgcolor("black")

myTurtle = turtle.Turtle()
myTurtle.color("brown", "blue")
myTurtle.left(90)
myTurtle.speed(0)
myTurtle.penup()
myTurtle.setpos(0, -250)
myTurtle.pendown()

tree(120, myTurtle)

window.exitonclick()