def personal_info(): #program that shows first and last name, address, phone number
    #and, what college major this person wants
    print("Taylor")
    print("Short")
    print("74 W. Shady St. Rossville, GA 307041")
    print("706-858-4395")
    print("Film editing")
    
def total_purchase():
    first = float(input("Please enter a price for your fisrt item: "))
    second = float(input("Please enter a price for your second item: "))
    third = float(input("Please enter a price for your third item: "))
    fourth = float(input("Please enter a price for your fourth item: "))
    fifth = float(input("Please enter a price for your fifth item: "))
    
    print("")
    
    subtotal = (first + second + third + fourth + fifth)
    print("Subtotal: $", subtotal)
    tax = (.07 * subtotal)
    print("Tax:      $", tax)
    total = (tax + subtotal)
    print("Total:    $", total)
    
def distance_traveled():
    speed = int(input("How fast are you driving? "))
    six = speed * 6
    print("At", speed, "miles per hour you will travel", six, "miles in 6 hours.")
    
    ten = speed * 10
    print("At", speed, "miles per hour you will travel", ten, "miles in 10 hours.")
    
    fifthteen = speed * 15
    print("At", speed, "miles per hour you will travel", fifthteen, "miles in 15 hours.")
    
def sales_tax():
    sale_amount = float(input("Enter the sale amount: "))
    
    state_tax = .05 * sale_amount
    county_tax = .025 * sale_amount
    total_tax = county_tax + state_tax
    total_sale = sale_amount + total_tax
    

    print("Your purchase price was: \t$", format(total_sale, '7.2f'))
    
    print("Your state tax amount is: \t$", format(state_tax, '7.2f'))
    
    print("Your county tax amount is: \t$", format(county_tax, '7.2f'))
    
    print("Your total tax is: \t\t$", format(total_tax, '7.2f'))
    
    print("Your total sale is: \t\t$", format(total_sale, '7.2f'))
    
def tip_tax_total():
    sale_amount = float(input("Please enter the sale amount: "))
    print("The sale was: \t\t\t$", format(sale_amount, '7.2f'))
    
    tip_amount = .18 * sale_amount
    sales_tax = .07 * sale_amount
    total_bill = (sales_tax + tip_amount + sale_amount)
    
    print("The tip amount is: \t\t$", format(tip_amount, '7.2f'))
    
    print("The sales_tax amount is: \t$", format(sales_tax, '7.2f'))
    
    print("The total bill is: \t\t$", format(total_bill, '7.2f'))
    
def temp_converter():
    degrees = int(input("Please enter the degrees Celsius: "))
    
    fahrenheit = (9/5) * degrees +32
    
    print(degrees, "degrees celsius is", fahrenheit, "degrees fahrenheit")
    
def cookie_monster():
    cookies = int(input("How many cookies do you want to make? "))
    print("For", cookies,"cookies you will need:")
    
    sugar_X = 1.5 / 24
    butter_X = 1 / 24
    flour_X = 2.75 / 24
    
    sugar_cups = (cookies * sugar_X) // 1
    butter_cups = (cookies * butter_X) // 1
    flour_cups = (cookies * flour_X) // 1
    
    sugar_oz = ((cookies * sugar_X) %1)*8
    butter_oz = ((cookies * butter_X) %1)*8
    flour_oz = ((cookies * flour_X) %1)*8
    
    print(sugar_cups, "cup(s)", sugar_oz, "ounces of sugar.")
    print(butter_cups, "cup(s)", butter_oz, "ounces of butter.")
    print(flour_cups, "cup(s)", flour_oz, "ounces of butter.")
    
def class_demographics():
    females = float(input("Enter the number of females: "))
    males = float(input("Enter the number of males: "))
    
    students = females + males
    con_f = females / students
    con_m = males / students
    
    print("The class consists of", format(con_f, '.0%'), "females and", format(con_m, '.0%'), "males.")
    
    
def tortuga_1():
    import turtle
    turtle.pensize(5)
    turtle.forward(155)
    turtle.write("E",font=(35))
    
    turtle.goto(0,0)
    turtle.left(90)
    turtle.forward(150)
    turtle.write("N",font=(35))
    
    turtle.goto(0,0)
    turtle.left(90)
    turtle.forward(155)
    turtle.write("W",font=(35))
    
    turtle.goto(0,0)
    turtle.left(90)
    turtle.forward(150)
    turtle.penup()
    turtle.forward(20)
    turtle.write("S", font=(35))
    turtle.pendown()
    
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.left(45)
    turtle.forward(125)
    
    turtle.goto(0,0)
    turtle.left(90)
    turtle.forward(125)
    
    turtle.goto(0,0)
    turtle.left(90)
    turtle.forward(125)
    
    turtle.goto(0,0)
    turtle.left(90)
    turtle.forward(125)
    

def tortuga_2():
    import turtle
    turtle.setup(800,600)
    turtle.penup()
    turtle.left(180)
    turtle.forward(160)
    turtle.right(90)
    turtle.forward(120)
    turtle.pendown()
    
    turtle.pensize(9)
    turtle.pencolor("light blue")
    turtle.circle(100)
    
    turtle.left(90)
    turtle.pencolor("yellow")
    turtle.circle(100)
    
    turtle.right(180)
    turtle.penup()
    turtle.forward(215)
    turtle.left(90)
    turtle.pendown()
    
    turtle.pencolor("black")
    turtle.circle(100)
    
    turtle.left(90)
    turtle.pencolor("green")
    turtle.circle(100)
    
    turtle.right(180)
    turtle.penup()
    turtle.forward(215)
    turtle.left(90)
    turtle.pendown()
    
    turtle.pencolor("red")
    turtle.circle(100)
