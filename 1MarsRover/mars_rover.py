import turtle

# Mission description at this link: https://www.101computing.net/mars-perseverance-rover/

# TODO: Set path to your images
image_path = "24_09_27/1MarsRover/mars_pics"


mission_images = [1,1,2,3,4,6,5]
mission_start_x = [-165,-165,-165,-165,-155,-165,-35]
mission_start_y = [-165,-165,-167,-169,-135,-165,-160]


# TODO: Set the mission you want to play (1-7)
mission = 4


# Setup screen size and background
screen = turtle.Screen()
screen.setup(410, 410)
screen.bgpic(image_path + "/mars-path-" +str(mission_images[mission - 1]) + ".png")

# Setup rover shape, pen color and pen size
rover = turtle.Turtle()
screen.register_shape(image_path + "/rover.gif")
rover.shape(image_path + "/rover.gif")
rover.color("#810000")
rover.speed(5)
rover.pensize(4)

# Put rover to start possition
rover.penup()
rover.goto(mission_start_x[mission-1],mission_start_y[mission-1])
rover.pendown()

# TODO: Here place your code for rover

cislo = 335
rover.forward(cislo)
for i in range(7):
    for i in range(2):
        rover.left(90)
        rover.forward(cislo)
    cislo -= 50




























def mission1():
    for i in range(4):
        rover.forward(350)
        rover.left(90)



def mission2():
    cislo = 1
    for i in range(8):
        rover.forward(335)
        rover.left(90*cislo)
        rover.forward(48)
        rover.left(90*cislo)
        cislo = cislo*-1








screen.mainloop() # keep the program running after the rover stops

# TIPS:
# Close window by Ctrl + C (kill program)
# Make a function for each mission
# Turtle library documentation: https://docs.python.org/3/library/turtle.html#  (Follow link: Cmd + click)
