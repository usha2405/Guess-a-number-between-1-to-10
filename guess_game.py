import random
x=None
y=None
r=random.randint(1,10)
x= int(input("guesss a number:"))
while y!='n':
    x= int(input("guesss a number:"))
    if (x>r):
        print("too high")
    elif (x==r):
        print("you guessed it correct")
    else:
       print("too low")         
    y=input('if continue press y and n to quit')

    

