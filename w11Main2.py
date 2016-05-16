import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
coord=[(100,100),(200,100)]
def keyup():
    t1.forward(50)
    curpos=t1.pos()
    isInRectangle(curpos,coord)

    
def keydown():
    t1.left(180)
    t1.forward(50)
    curpos=t1.pos()
    isInRectangle(curpos,coord)

    
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
    if xs <= curpos[0] <= xe and ys-100 <=curpos[1] <= ye+100:
        t1.pencolor("Red")
    
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