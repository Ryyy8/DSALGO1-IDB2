"""#this is a comment

x = 1                  #integer
y = 2.0                 #real number
z = x * y
print("1 x 2.0 = ", z, "\n This is a test for my python program!")
print("\n This is another line")

userInput = input("How old are you?") #accepting an input with a prompt message
print(userInput,"years old!")         #prints out the user input

userInput = input("Enter a number: ")
userInput2 = input("Enter a number again: ")
sum = int(userInput) + int(userInput2)
print("The sum is: ",sum)

"""
"""import math

nintendoWiss = 100
money = input("How much is your money?")
personCanAfford = float(money) / int(nintendoWiss)
additionalWii =  abs((int(money) % int(nintendoWiss)) - nintendoWiss)
print("You can afford: ", math.floor(personCanAfford),"piece/s of Nintendo Wiis")
print("You will need", additionalWii, "pesos to afford an additional Wii")"""


"""fact = 1
userInput = int(input("Enter a number: "))
for i in range(1, userInput+1):
    fact = fact * i
print("The factorial of", userInput, "is", fact)"""

factorList = []
userInput = int(input("Enter a number: "))
for a in range(1, userInput+1):
    if userInput % a == 0:
        factorList.append(a)
print ("The factor of", userInput, "are: ", factorList)






