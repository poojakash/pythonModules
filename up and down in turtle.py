#up down is used to make pen up and down to add diagram in same programm
import turtle
t=turtle.Pen()
for i in range(0,8):
    t.forward(80)
    t.left(45)
t.up()
t.right(90)
t.forward(90)
t.down()
for i in range(0,8):
    t.forward(80)
    t.left(45)
