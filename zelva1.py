import turtle
import os
os.system ("cls")

def ctverec():

    def ziskejUdaje():
        velikost = int (input("velikost ctverce:"))
        
        x = int (input("pozice x"))
        y = int (input("pozice y"))
        return velikost,x,y
    velikost,x,y = ziskejUdaje()
    
    turtle.penup()
    
    turtle.goto(x,y)

    turtle.setheading(180)
    turtle.forward(velikost/2)
    turtle.setheading(90)
    turtle.forward(velikost/2)

    turtle.setheading(0)

    turtle.pendown()

    for i in range(4):
        turtle.forward(velikost)
        turtle.right(90)




def trojuhelnik():
    def ziskejUdaje():
        velikost = int (input("velikost trojuhelnik:"))
        
        x = int (input("pozice x"))
        y = int (input("pozice y"))
        return velikost,x,y
    velikost,x,y = ziskejUdaje()

    turtle.penup()
    
    turtle.goto(x,y)

    turtle.pendown()
    
    turtle.setheading(60)
    turtle.forward(velikost)
    
    for i in range(3):
        turtle.right(60)
        turtle.forward(velikost)

def domek():
    ...


print("co chces postavit?")
vyberStavby = int (input("1 = ctverec"))
if vyberStavby == 1:
    ctverec()






turtle.mainloop()