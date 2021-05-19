# Write a program to check the great among 3 numbers
listOfNums = [32, 83, 92]

def findMax(list):
  max = list[0]
  for i in range(len(list)):
    if(list[i] > max):
      max = list[i]
  print(max)

findMax(listOfNums)

def trafficLight(String):
  if (String == "red"):
    print("You must stop!")
  elif (String == "green"):
    print("You can go!")
  elif (String == "yellow"):
    print("You can go, but hurry the heck up!")

trafficLight("green")
trafficLight("red")
trafficLight('yellow')

