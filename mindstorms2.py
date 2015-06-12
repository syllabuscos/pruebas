import turtle

def draw_square(some_turtle):
    # The form
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)
        
        
def draw_art():
    # Creating the screen as background
    window = turtle.Screen()
    window.bgcolor("red")
    # Grabbing our turtle
    brad = turtle.Turtle()
    # Customizing
    brad.shape("turtle")
    brad.color("black")
    brad.speed(2)
    draw_square(brad)
    
    # Now the one that creates the circle
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue")
    angie.circle(100)
    
    # Now the triangle
    bill = turtle.Turtle()
    bill.shape("turtle")
    bill.color("green")
    
    for j in range(0,3):
        bill.forward(100)
        bill.right(120)
        
    # Exit when clic
    window.exitonclick()
    
    
draw_art()
