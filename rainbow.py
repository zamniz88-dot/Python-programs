import turtle
tb= turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'purole', 'blue', 'green', 'orange', 'yellow']
s.bgcolor('black')
t.speed('faster') # type: ignore
t.hideturtle() # type: ignore
while True:
   for x in range(200):
      t.pencolor(colors[x%len(colors)]) # type: ignore
      t.width(x/100 + 1) # type: ignore
      t.forward(x) # type: ignore
      t.left(59) # type: ignore
    t.right(239) # type: ignore
for x in range(200, 0, -1):
   t.pencolor('black')
   t.width(x/100 + 7)
   t.forward(x)
   t.right(59)