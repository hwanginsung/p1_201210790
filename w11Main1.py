import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def keyup():
    t1.forward(50)
def keydown():
    t1.left(180)
    t1.forward(50)
def keyleft():
    t1.left(90)
def keyright():
    t1.right(90)

def mousegoto(x,y):
    t1.setpos(x,y)

def exit():
    wn.bye()
def byeBye():
    wn.onkey(exit,"q")

def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")
def addMouse():
    wn.onclick(mousegoto)

def lab11():
	addkeys()
	addMouse()
	byeBye()
	wn.listen()
	turtle.mainloop()

lab11()
