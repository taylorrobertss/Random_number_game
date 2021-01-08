#from random import seed
from random import randint

print("Welcome to the random number generator game ")
value=randint(0,20)
count=0
usernum= int(input("Please enter a number between 0 and 20\n"))

while usernum != value:
    if usernum> value:
       usernum= int(input("Your guessed number is too high, please try again soon!\n"))
       

    if usernum < value:
        usernum=int(input("Your guessed number is too low, please try again!\n"))
    count+=1

if usernum== value:
    count+=1
    print("You guessed correctly\n It took you %d tries"%(count))

