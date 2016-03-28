import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def makeSwirlSquares(size,bigger,sides,angle):
    t1.home()
    t1.clear()
    for i in range(0,sides):
        if (i%2):
            size=size+bigger
        t1.forward(size)
        t1.right(angle)
        
makeSwirlSquares(10,10,10,90)

wn.exitonclick()