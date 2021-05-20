# Create a while loop that goes through the 12 days of christmas

from typing import Tuple


trueLoveGifts = ["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7", "item 8", "item 9", "item 10", "item 11", "item 12", ]

def twelveDaysOfChristmas():
  j = 0
  i = 1
  while(i <= 12):
    print(f"On the {i} day of Christmas, my true love gave to me {trueLoveGifts[j]}")
    i += 1
    j +=1

# twelveDaysOfChristmas()


# Create a list and pass it in as a parameter and return the sum of the list

myList2 = [23, 43, 13, 535, 32]
myList3 = [1, 3, 2, 4]

def sumOfList(list):
  sum = 0
  i = 0
  while(i < len(list)):
    sum += list[i]
    i += 1
  print(sum)
  return sum

# sumOfList(myList2)
# sumOfList(myList3)

# Create a for loop that goes through the 12 days of christmas

def twelveDaysOfChristmasForLoop():
  for i in range(1, 12):
    print(f"On the {i} day of Christmas, my true love gave to me {trueLoveGifts[i - 1]}")

twelveDaysOfChristmasForLoop()

# Create a list and pass it in as a paramete and return the sum 

def sumOfListForLoop(list):
  sum = 0
  for i in range(len(list)):
    sum += list[i]
  print(sum)
  return sum

sumOfListForLoop(myList2)
sumOfListForLoop(myList3)


