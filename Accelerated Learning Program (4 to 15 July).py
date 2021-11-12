import click
import math

def s():
    print ("  ")


def l():
    print ("--------------------")
    
print(
    "Hello, this is all the code done from July 4 to July 13, 2021!                                                             by Arnav"
)
print("                                             ")
if click.confirm(f"Do you want to start?", default=True):
    s()
    print("Ok! Let's start!")
    print("...")
    print("Choose a date:")
    print("1) July 4")
    print("2) July 4 continued")
    print("3) July 5")
    print("4) July 6")
    print("5) July 7")
    print("6) July 10")
    print("7) July 11")
    print("8) July 11")
    print("9) July 13")
    print("10) July 14")


    s()


    
    
    action = int(input("Enter option number here (1/2/3/4/5/6/7/8/9/10/11): "))
    
    

def switch(action):
    if action == 1:
        
       print ("Work done on July 4.")

    
       FavNumber = int(input("Hi! What's your favorite number? "))

       s()

       print (f"Alright! So your favorite number is {FavNumber}!")

       print ("Learning Python", end = " ")
       print ("Developed by Guido Van Rossum")

       s()
       l()
       s()

       n = int(input("Enter any number: "))
       d_n = n * 2
       print ("Double of", n, "is", d_n)

       s()


       x, y = 8, 2
       x, y = y, x+2
       print (x, y)

       x1, y1 = 7, 2

       x1, y1, x1 = x1+4, y1+6, x1+100
       print(x1,y1)

    

       try:

          n1 = int(input("Enter a number: "))
          n2 = int(input("Enter another number: "))

          print(n1/n2)

       except:

          print ("Dividing by zero? Nope! Can't do it!")



if action == 2:
    print ("Work done on July 4 continued.")
    
    try:

          n1 = int(input("Enter a number: "))
          n2 = int(input("Enter another number: "))

          print(n1/n2)

    except:

          print ("Dividing by zero? Nope! Can't do it!")


        
if action == 3:
    print ("Work done on July 5.")

    bonus = 0

    sale = float(input("Enter Monthly Sales you fulfilled: "))

    if  sale > 50000:
        bonus = sale * 10/100
        print ("Your bonus is", str(bonus))

    if sale < 50000:
        print ("Sorry, you're not eligible for a bonus :(")


        aL1 = float(input("Please input any number here: "))
        aL2 = float(input("Please input another number here: "))

        if aL1 > aL2:
            print (aL1, "is larger than", aL2)

        if aL2 > aL1:
            print (aL2, "is larger than", aL1)


if action == 4:                             
    print ("Work done on July 6.")

    
    nL1 = int(input("Please input any number here: "))
    nL2 = int(input("Please input another number here: "))
    nL3 = int(input("Please input one more number here: "))

    if nL1 > nL2 > nL3:
     print (nL1, "is larger than", nL2, ">", nL3)

    if nL2 > nL1 > nL3:
     print (nL2, "is larger than", nL1, ">", nL3)

    if nL3 > nL2 > nL1:
     print (nL3, "is larger than", nL2, ">", nL1)

    if nL2 > nL3 > nL1:
     print (nL2, "is larger than", nL3, ">", nL1)

    if nL1 > nL3> nL2:
     print (nL1, "is larger than", nL3, ">", nL2)



    age1 = int(input("Please enter your age: "))

    if age1 > 18:
        print (f"You're eligible to vote since you're {age1} years old!")

    if age1 < 18:
        print (f"Sorry, you can't vote just yet :( Come back after {18-age1} years!")

            

        
        
if action == 5:                             
    print ("Work done on July 7.")

    num111 = int(input("Enter any number: "))

    if num111%2 == 0:
        print (f"{num111} is an even number!")

    else:
        print (f"{num111} is an odd number!")

    s()

    T_age = int(input("Please enter your age: "))

    if T_age >= 13 and T_age <= 20:
        print (f"You're a Teenager! Enjoy!")

    else:
        print ("You are not a Teenager :(")


    s()
    
    bonus = 0
    sale1 = float(input("Enter Monthly Sales you fulfilled: "))

    if  sale1 > 500000:
        bonus = sale1 * 10/100
        print ("Your commission is 10%!", bonus, " AED is your commission!")

    if sale1 < 500000:
        bonus = sale1 * 5/100
        print ("Your commission is 5%!", bonus, " AED is your commission!")


    s()
    
       
if action == 6:                             
    print ("Work done on July 10.")

    print ("Let's find square roots!")
    l()
    sqrtn1 = float(input("Enter any number to find its square root: "))
    sqrt = math.sqrt(sqrtn1)
    print (f"The square root of {sqrtn1} is {sqrt}!")
    s()
    l()
    s()
    print ("Welcome to the Quadratic Equations solver!")
    s()
    Qa = float(input("Input the value of a from the equation: "))
    Qb = float(input("Input the value of b from the equation: "))
    Qc = float(input("Input the value of c from the equation: "))

    l()

    if Qa == 0:
        print ('Hey! The value of "a" can not be zero!')
        exit()

    DiscR = Qb*Qb - 4 * Qa * Qc

    

    if DiscR > 0:
        print ("Finding roots...")
        l()
        Rt1 = ((-Qb) + math.sqrt(DiscR)) / 2*Qa
        Rt2 = ((-Qb) - math.sqrt(DiscR)) / 2*Qa
        print (f"There are 2 roots for this equation! They are {Rt1} and {Rt2}")

    if DiscR == 0:
        print ("Finding roots...")
        l()
        Rt3 = (-Qb) / 2*qa
        print (f"There is 1 root for this equation! It is {Rt3}")

    if DiscR < 0:
        print ("This equation has no real roots")

        
    


if action == 7:                             
    print ("Work done on July 11.")

    s()
    print("All marks are out of 100")
    l()
    S1 = int(input("Enter your marks for subject 1: "))
    S2 = int(input("Enter your marks for subject 2: "))
    S3 = int(input("Enter your marks for subject 3: "))
    S4 = int(input("Enter your marks for subject 4: "))
    S5 = int(input("Enter your marks for subject 5: "))

    S_total = S1 + S2 + S3 + S4 + S5
    S_avg = S_total/5

        
    print (f"Your total percentage is {S_avg}%!")
    

    if S_avg >=90:
        print("Your grade is A+!")

    elif S_avg >=75:
        print("Your grade is A!")
            
    elif S_avg >=60:
        print("Your grade is B+!")

    elif S_avg >=45:
        print("Your grade is B!")

    elif S_avg >=40:
        print("Your grade is C!")

    elif S_avg >=35:
        print("Your grade is D!")

    else:
        print("Your grade is F! Time to  work harder!")


    s()
    l()
    s()

    pn1 = float(input("Enter any number here, I'll let you know if its positive or negative: "))

    if pn1 == 0:
        print ("You have entered zero. Zero isn't a positive or negative number. ")

    elif pn1 > 0:
        print ("You have entered a positive number!")

    elif pn1 < 0:
        print ("You have entered a negative number!")

    else:
        print ("Please enter a valid number!")


    s()
    l()
    s()

    bill_amount = float(input("Enter your bill amount here: "))

    if bill_amount >= 20000:
        print("You're eligible for a 15% discount!")
        
        discfif = bill_amount * 15/100
        final15 = bill_amount - discfif
        print(f"Your 15% discount is {discfif}! You only need to pay {final15}!")
        
    elif bill_amount >= 15000:
        print("You're eligible for a 10% discount!")
        
        disc10 = bill_amount * 10/100
        final10 = bill_amount - disc10
        print(f"Your 10% discount is {disc10}! You only need to pay {final10}!")

    elif bill_amount >= 10000:
        print("You're eligible for a 5% discount!")
        
        disc5 = bill_amount * 5/100
        final5 = bill_amount - disc5
        print(f"Your 5% discount is {disc5}! You only need to pay {final5}!")

    else:
        print ("Well, its sad that you don't qualify for a discount, but you're lucky your bill is already under 10,000!")


    s()
    l()
    s()


    yr = int(input("Enter any year: "))

    if yr % 100 == 0:
        if yr % 400 == 0:
            print(f"{yr} is a leap year!")
        else:
            print(f"{yr} is not a leap year :(")

    elif yr % 4 == 0:
            print (f"{yr} is a leap year with a day extra! Enjoy!")

    else:
            print (f"{yr} is not a leap year :(")

    s()
    l()
    s()

    Ln1 = float(input("Enter any number: "))
    Ln2 = float(input("Enter another number: "))
    Ln3 = float(input("Enter one more number: "))

    if Ln1 > Ln2 > Ln3:
        print (f"{Ln1} is larger than {Ln2} and {Ln3} is the smallest number here!")

    elif Ln3 > Ln2 > Ln1:
        print (f"{Ln3} is larger than {Ln2} and {Ln1} is the smallest number here!")

    elif Ln2 > Ln1 > Ln3:
        print (f"{Ln2} is larger than {Ln1} and {Ln3} is the smallest number here!")

    elif Ln3 > Ln1 > Ln2:
        print (f"{Ln3} is larger than {Ln1} and {Ln2} is the smallest number here!")

    elif Ln1 > Ln3 > Ln2:
        print (f"{Ln1} is larger than {Ln3} and {Ln2} is the smallest number here!")

    elif Ln2 > Ln3 > Ln1:
        print (f"{Ln2} is larger than {Ln3} and {Ln1} is the smallest number here!")
        

if action == 8:                             
    print ("Work done on July 12.")

    N_day = int(input("Enter a number from 1 to 7: "))
    
    if N_day == 1:
        print ("Sunday")

    elif N_day == 2:
        print ("Monday")

    elif N_day == 3:
        print ("Tuesday")

    elif N_day == 4:
        print ("Wednesday")

    elif N_day == 5:
        print ("Thursday")

    elif N_day == 6:
        print ("Friday")

    elif day == 7:
        print ("Thursday")

    else:
        print ("Please enter a number between 1 to 7")
        

if action == 9:                             
    print ("Work done on July 4.")


        
if action == 10:                             
    print ("Work done on July 4.")


if action == 11:
    print ("Work done on July 13.")
    

    if action not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        print("No such option exists! Choose an option between 1 and 11 [Rerun the program]")
    else:
        switch(action)

        


