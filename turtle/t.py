import turtle
# fred = turtle.Turtle()
# fred.color("red")
# fred.forward(100)
# fred.right(135)
# fred.forward(140)
# fred.right(135)
# fred.forward(100)
def shapeRnS(sides):
    'function to draw similar sized shap by having a relation between circumference and radius C = 2 pi R '
    t = turtle.Turtle()
    t.color("magenta")
    t.width(5)

    for side in range(sides):
        t.forward(360 / sides)
        t.right(360 / sides)

def spiral():
    t = turtle.Turtle()
    t.color("cyan")

    for side in range(20):
        t.forward(side * 10)
        t.right(120)

t = turtle.Turtle()
t.speed(0)
t.width(4)

def tri():
    for s in range(3):
        t.forward(100)
        t.right(120)

def cycle():
    for color in ['red', 'orange', 'blue']:
        t.color(color)
        for i in range(6):
            tri()
            t.right(360/18)
    t.hideturtle()
# Call the function multiple times.

# cycle()
# t.penup()
# t.pendown()
# t.home()
# t.back()
