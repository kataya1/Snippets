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