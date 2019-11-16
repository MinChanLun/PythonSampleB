import turtle
from turtle import *

star = turtle.Turtle()
window = turtle.Screen()

window.bgcolor("#ffffff")
star.color('#ffcc00', '#00007f')

begin_fill()
# while True:	
for i in range(5):
	star.forward(100)
	star.right(144)
	if abs(pos()) < 1 :
	 	break


end_fill()

turtle.done()