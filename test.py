def comment_example():
    #comment example receives no arguments
    #it explains how to creat a function header
    #and outputs or returns "Hello World!"
    print('hello world!')
    
def program2_1(): #apostrophe output
    print('Kate Austen')
    print('123 Full Cirlce Drive')
    print('Asheville, NC 28899')
    
def program2_2(): #double quote output
    print("Kate Austen")
    print("123 Full Cirlce Drive")
    print("Asheville, NC 28899")
    
def program2_3(): #output and retutns "Don't fear!" "I'm here"
    print("Don't fear!")
    print("I'm here")

def program2_4():
    print('Your assignment is to read "Hamlet" by tommorrow.')
    
def program2_5(): #apostrophe output
    #This function displays a person's name and address
    print('Kate Austen')
    print('123 Full Cirlce Drive')
    print('Asheville, NC 28899')

def program2_6(): #apostrophe output
    print('Kate Austen') #Display the Name
    print('123 Full Cirlce Drive') #Display the address
    print('Asheville, NC 28899') #Display the city, state, and ZIP
    
def program2_7(): #variable demo 1
    #This program demonstrates a variable
    print('I am staying in room number')
    room = 503
    print(room)
    
def program2_8():
    top_speed = 160
    print('The top speed is')
    print(top_speed)
    distance = 300
    print('The distance traveled is')
    print(distance)
    
def program2_9(): #variable demo 3
    #This program demonstrates
    room = 503
    print('I am stayingin room number', room)

def program2_10():
    account = 2.75
    print('I have', account, 'im my account.')
    account += 97.2
    print ('But know I have', account, 'in my account')
    
def program2_11(): #string variable
    #Creat variables to reference two strings
    first = "Kathryn"
    last = "Marino"
    #Display the values referenced by the variables
    print(first, last)

def program2_12():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    print('Hello', first, last)
    
def program2_13():
    name = input('What is your name? ')
    age = int(input('What is your age? '))
    income = float(input('What is your income? '))
    
    print('Here is the data you entered:')
    print('Name: ',name)
    print('Age: ',age)
    print('Income: ',income)

def program2_14(): #simple math
    #Assign a value to the salary variable
    salery = 2500.00
    
    #Assign a value to the bonus variable
    bonus = 1200.00
    
    #Calculate the total pay = salery + bonus
    pay = salery + bonus
    
    #Display the pay
    print('Your pay is',pay)
    
def sale_price():
    original_price = float(input("Enter the item's original price: "))
    
    discount = original_price * .2
    sale_price = original_price - discount
    
    print("The sale price is ", sale_price)
    
def program2_16():
    first_score = float(input("Enter the first test score: "))
    second_score = float(input("Enter the seocnd test score: "))
    third_score = float(input("Enter the third test score: "))
    
    average = (first_score + second_score + third_score) / 3
    print("The average score is:", average)
    
def program2_17():
    total_seconds = float(input("Enter the number the seconds: "))
    total_hours = total_seconds // 3600
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60
    
    print("Here is the time in hours, minutes, and seconds:")
    print("Hours: ", total_hours)
    print("Minutes: ", minutes)
    print("Seconds: ", seconds)
    
def program2_18():
    future_value = float(input("Enter the desired future value: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    years = float(input("Enter the number of years the will grow: "))
    deposit = future_value / ((1 + interest_rate)**years)
    print("You will need to deposit ", format(deposit, '.2f'), sep='$')
    
def program2_19():
    payment = 5000
    monthly_payment = payment / 12
    print("The monthly payment is ", monthly_payment)
    
def program2_20():
    payment = 5000
    monthly_payment = payment / 12
    print("The monthly payment is ", format(monthly_payment, '.2f'))
    
def program2_21():
    monthly_payment = 5000
    annual_pay = monthly_payment * 12
    print('Your pay is $', format(annual_pay, '.2f'), sep='')
    
def program2_22():
    num1 = 127.899
    num2 = 3465.148
    num3 = 3.776
    num4 = 264.821
    num5 = 88.081
    num6 = 799.999
    
    print(num1, '7.2f')
    print(num2, '7.2f')
    print(num3, '7.2f')
    print(num4, '7.2f')
    print(num5, '7.2f')
    print(num6, '7.2f')