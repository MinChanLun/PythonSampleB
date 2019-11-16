import turtle
from turtle import *

window = turtle.Screen()
#window.bgcolor("#00ffbb")
window.bgpic("irene.gif")

color('#5e5e5e', '#f90000')
begin_fill()
while True:	
	forward(200)
	left(120)
	
	if abs(pos()) < 1:
		break


end_fill()
done()