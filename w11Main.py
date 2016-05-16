import turtle
wn=turtle.Screen()
wn.bgpic("C:\Users\P400\Desktop\myMaze.gif")
t1=turtle.Turtle()
t1.speed(1)
t1.penup()
t1.goto(-400,300)
t1.pendown()
t1.pencolor("Red")

def mousegoto(x,y):
    t1.setpos(x,y)

def exit():
    wn.bye()
def byeBye():
    wn.onkey(exit,"q")
    
def addMouse():
    wn.onclick(mousegoto)

addMouse()
wn.listen()
turtle.mainloop()