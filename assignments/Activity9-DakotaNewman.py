# Write a function that given a list will print out all the values in that list

myList = ["Dakota", 28, "Married"]

for i in myList:
 print(i)

# or 

for i in range(len(myList)):
  print(myList[i])


# Write a function that takes in one integer as a parameter and will print out your name as many times as specified by the argument.

def printName(num):
  print("Dakota" * num)

printName(20)