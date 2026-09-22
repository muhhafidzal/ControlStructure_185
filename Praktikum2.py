#answer=input("Would you like express shipping? (yes/no): ")
#if answer > "yes" :
#    print("That will be an extra Rp. 10.000,-")
#else:
#   print("OK no worry")

#deposit = 100
#if deposit > 100:
#    print("You get a free toaster!")
#else:
#   print("You get a free mug!")
#print("Have a nice day!")
#
#import turtle
#turtle.color("green")
#turtle.forward(120)
#turtle.right(45)
#turtle.color("blue")
#turtle.forward(120)
#turtle.right(45)
#turtle.color("pink")
#turtle.forward(120)
#turtle.right(45)
#turtle.color("yellow")
#turtle.forward(120)
#turtle.right(45)
#turtle.color("red")
#turtle.forward(120)
#turtle.right(45)
#turtle.color("black")
#turtle.forward(120)
#turtle.right(45)
#turtle.color("black")
#turtle.forward(120)
#turtle.right(45)
#turtle.color("black")
#turtle.forward(120)
#turtle.right(45)

#answer = "0"
#
#while answer != "4" :
#    answer = input("What is 2 + 2 =? ")
#    print("Sorry, Try Again!")
#print ("Yes! 2 + 2 = 4")

import turtle 
nbrSides = 6
for steps in range (nbrSides):
    turtle.forward(100)
    turtle.right(360/nbrSides)
    for morestep in range(nbrSides):
        turtle.forward(50)
        turtle.right(360/nbrSides)
