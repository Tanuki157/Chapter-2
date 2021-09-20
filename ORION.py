import turtle
def orion():
    turtle.setup(500,600)
    turtle.penup()
    turtle.hideturtle()
    
    LEFT_SHOULDER_X = -70
    LEFT_SHOULDER_Y = 200
    
    RIGHT_SHOULDER_X = 80
    RIGHT_SHOULDER_Y = 180
    
    MIDDLE_BELTSTAR_X = -40
    MIDDLE_BELTSTAR_Y = -20
    
    LEFT_BELTSTAR_X = -40
    LEFT_BELTSTAR_Y = -20
    
    RIGHT_BELTSTAR_X = 40
    RIGHT_BELTSTAR_Y = 20
    
    LEFT_KNEE_X = -90
    LEFT_KNEE_Y = -180
    
    RIGHT_KNEE_X = -120
    RIGHT_KNEE_Y = -140
    
    #Turtle starts at the left shoulder
    #makes a dot and names it Betelguese
    turtle.goto(-70, 200)
    turtle.dot()
    turtle.write("Betelguese")
    turtle.pendown()
    turtle.showturtle()
    
    #Turtle gos to the left beltstar makes
    #a dot and names it Alnitak
    turtle.goto(-40, -20)
    turtle.dot()
    turtle.write("Alnitak")
    
    #Turtle goes to the left knee makes a
    #dot then names it Saipha
    turtle.goto(-90, -180)
    turtle.dot()
    turtle.write("Saipha")
    
    #After the finishing the left side picks up the pen
    #then goes to the right shoulder
    #puts the pen down,dots it, name it Meissa
    turtle.penup()
    turtle.goto(80, 180)
    turtle.pendown()
    turtle.dot
    turtle.write("Meissa")
    
    #Turtle goes to right beltstar, dots,
    #then names it Mintaka
    turtle.goto(40, 20)
    turtle.dot()
    turtle.write("Mintaka")
    
    #Turtle goes to right knee, dots, then
    #names it Rigel
    turtle.goto(120, -140)
    turtle.dot()
    turtle.write("Rigel")
    
    #Turtle pick up the pen then goes to
    #right beltstar, puts the pen down
    #then makes a line through the middle
    #after that goes to the middle, dots it
    #then name it Alnitam
    turtle.penup()
    turtle.goto(40, 20)
    turtle.pendown()
    turtle.goto(-40, -20)
    turtle.goto(0, 0)
    turtle.dot()
    turtle.write("Alnitam")
    
    turtle.hideturtle()
    turtle.done()