import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
coord=[(100,100),(200,200)]
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
    curpos=t1.pos()
    isInRectangle(curpos,coord)


def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    if xs <= curpos[0] <= xe and ys <=curpos[1] <= ye:
        t1.pencolor("Red")
    
def exit():
    wn.bye()
def byeBye():
    wn.onkey(exit,"q")

def addkeys():
    wn.onkey(keyup,"Up")
    curpos=t1.pos()
    isInRectangle(curpos,coord)
    wn.onkey(keydown,"Down")
    curpos=t1.pos()
    isInRectangle(curpos,coord)
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")
def addMouse():
    wn.onclick(mousegoto)
    curpos=t1.pos()
    isInRectangle(curpos,coord)

def lab11():
    addkeys()
    addMouse()
    byeBye()
    wn.listen()
    turtle.mainloop()

lab11()