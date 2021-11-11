#Holiday Homework for Computer Science by Arnav
  
import click 
import math 
  
def s(): 
    print ("  ") 
  
  
def l(): 
    print ("--------------------") 
     
print("This is the holiday homework of Computer Science by Arnav Verma 11 M") 
s() 
l() 
s() 
if click.confirm(f"Do you want to start?", default=True): 
    s() 
    print("Ok! Let's start!") 
    print("...") 
    print("Choose a topic:") 
    print("1) IF Statements") 
    print("2) IF ELSE Statements") 
    print("3) IF-ELIF-ELSE Ladder") 
    print("4) FOR Loops") 
    print("5) WHILE Loops") 
    print("6) NESTED Loops") 
    print("7) Menu Driven") 
  
  
  
    s() 
     
     
    action = int(input("Enter option number here (1/2/3/4/5/6/7): ")) 
     
def switch(action): 
    if action == 1: 
  
       s() 
       print ("1. Simple Bonus finder using two if statements") 
       s() 
  
       sale1 = float(input("Enter Monthly Sales you fulfilled (in $): ")) 
       s() 
  
       commission = 0 
  
       if sale1 > 5000: 
          commission = sale1 * 10/100 
          print (f"You are eligible for a 10% commission! ${commission} is your commission earned!") 
  
       if sale1 < 5000: 
          commission = sale1 * 5/100 
          print (f"You are eligible for a 5% commission! ${commission} is your commission earned!") 
  
     
       s() 
  
if action == 2: 
  
    s() 
  
    print ("1. Even/Odd number program using if else statements") 
    eveodd = int(input("Enter any number: ")) 
  
    if eveodd%2 == 0: 
        print (f"{eveodd} is an even number!") 
  
    else: 
        print (f"{eveodd} is an odd number!") 
  
    s() 
  
    l() 
    s() 
  
    print ("2. Finding the largest number out of three numbers") 
    l() 
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
  
    else: 
        print ("hmm... I don't get it, try again please :) ") 
  
    print("The elif statement was also used above.") 
  
    s() 
    l() 
  
if action==3: 
    l() 
    print ("1. Finding the type of the triangle with three sides provided") 
    s() 
     
    s1 = float(input("Enter the length of the first side of the triangle: ")) 
    s() 
    s2 = float(input("Enter the length of the  second side of the triangle: ")) 
    s() 
    s3 = float(input("Enter the length of the third side of the triangle: ")) 
    s() 
  
    if s1==s2==s3: 
        print("This triangle is an Equilateral triangle since all three sides are equal!") 
  
    elif s1==s2 or s2==s3 or s3==s1: 
        print("This triangle is an Isoceles triangle since two sides are equal") 
  
    else: 
        print("This is either a Scalene or invalid triangle") 
     
  
    s() 
    l() 
    print("2. Calculating the roots of the quadratic equation in the form of ax^2 + bx + c = 0") 
  
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
        Rt3 = (-Qb) / 2*Qa 
        print (f"There is 1 root for this equation! It is {Rt3}") 
  
    if DiscR < 0: 
        print ("This equation has no real roots") 
  
  
    l() 
  
    print("3. Program to identify two numbers and an arithmetic operator and display the results") 
  
    One = int(input("Enter any number: ")) 
    Two = int(input("Enter another number: ")) 
    operator = (input("Enter any arithmetic operator (+, -, *, /): ")) 
                    
    if operator=="+": 
        s() 
        print(f"Ok, so you'll add!\nHere is the answer :) \n{One+Two}") 
  
    elif operator=="-": 
        s() 
        print(f"Ok, so you'll subtract the first number from the second one!\nHere is the answer :) \n{One-Two}") 
  
    elif operator=="*": 
        s() 
        print(f"Ok, so you'll multiply!\nHere is the answer :) \n{One*Two}") 
  
    elif operator=="/": 
        s() 
        print(f"Ok, so you'll divide the first number by the second one!\nHere is the answer :) \n{One/Two}") 
  
    else: 
        s() 
        s() 
        print("I didn't get that, please try again! :)") 
  
  
    l() 
  
    print("4. Grade calculation program") 
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
  
  
    l() 
  
    print ("5. Arranging three numbers in ascending order") 
    l() 
    AN1 = float(input("Enter any number: ")) 
    AN2 = float(input("Enter another number: ")) 
    AN3 = float(input("Enter one more number: ")) 
  
    if AN1 > AN2 > AN3: 
        print (f"{AN3} < {AN2} < {AN1} :)") 
  
    elif AN3 > AN2 > AN1: 
        print (f"{AN1} < {AN2} < {AN3} :)") 
  
    elif AN2 > AN1 > AN3: 
        print (f"{AN3} < {AN1} < {AN2} :)") 
  
    elif AN3 > AN1 > AN2: 
        print (f"{AN2} < {AN1} < {AN3} :)") 
  
    elif AN1 > AN3 > AN2: 
        print (f"{AN2} < {AN3} < {AN1} :)") 
  
    elif AN2 > AN3 > AN1: 
        print (f"{AN1} < {AN3} < {AN2} :)") 
  
    else: 
        print ("hmm... I don't get it, please try again :)") 
  
  
  
if action==4: 
    l() 
    print("Coming Soon") 
  
  
if action==5: 
    l() 
    print("Coming Soon") 
  
if action==6: 
    l() 
    print("Coming Soon") 
     
if action==7: 
    l() 
    print("1. Menu driven program to calculate the area of a Circle, Triangle, Square and Rectangle") 
  
  
    def switch(option): 
        if option == 1: 
            print("We will be finding the area of a circle using its radius.") 
  
            pi = 3.1415926535 
            rd = float(input("Please enter the radius of the circle: ")) 
            aC = pi*rd*rd 
            print ("Calculating area...") 
            print (f"The area of the circle is {aC} units!") 
            l() 
         
        
        if option == 2:                              
            print("We will be finding the area of a triangle using its base and height.") 
  
            bst = float(input("Please enter the base length of the triangle: ")) 
            hst = float(input("Please enter the triangle's height: ")) 
            arT = 1/2 * bst * hst         
  
            print ("Calculating area...") 
            print (f"The area of the triangle is {arT} units!") 
            l() 
  
        if option == 3: 
            print("We will be finding the area of a square using any of its sides.") 
  
            sS = float(input("Please enter the square's side length: ")) 
             
            arS = sS * sS      
  
            print ("Calculating area...") 
            print (f"The area of the square is {arS} units!") 
            l() 
  
        if option == 4:                              
            print ("We will be finding the area of a rectangle using its length and breadth.") 
            lN = float(input('Type the value of the length here: ')) 
            b = float(input('Type the value of the breadth here: ')) 
  
            lNxb = lN*b 
            print(f"The area of the rectangle is {lNxb} square units") 
            l() 
  
  
     
  
        if click.confirm(f"Do you want to start?", default=True): 
            print("       ") 
            print("Ok! Let's start!") 
            l() 
            print("Choose an option:") 
            s() 
            print("1) Finding the area of a Circle") 
            print("2) Finding the area of a Triangle") 
            print("3) Finding the area of a Square") 
            print("4) Finding the area of a Rectangle") 
  
        option = int(input("Enter option number here (1/2/3/4): ")) 
  
  
  
        if option not in [1, 2, 3, 4]: 
            print("No such option exists! Choose an option between 1 and 4 [Rerun the program]") 
        else: 
            switch(option) 
  
  
     
  
  
if action not in [1, 2, 3, 4, 5, 6, 7]: 
    print("No such option exists! Choose an option between 1 and 7 [Rerun the program]") 
else: 
    switch(action) 
  
#END of Code 
#Thank you for going through my code :) 
