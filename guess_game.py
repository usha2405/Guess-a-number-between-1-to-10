import random
x=None
y=None
r=random.randint(1,10)
x= int(input("Guesss a number:"))
while y!='n':
    x= int(input("Guesss a number:"))
    if (x>r):
        print("Too high")
    elif (x==r):
        print("You guessed it correct.")
    else:
       print("Too low")
    y=input('If continue press y and n to quit')
