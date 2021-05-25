# Activity 9.1
# Create a function that is given a list of numbers as a parameter and sort from least to greastest

myNumList = [324, 4515, 9]

def sortNumList(list):
  newList = []
  smallestNum = list[0]
  largestNum = list[0]
  middleNum = list[0]
  for i in range(len(list)):
    if(list[i] < smallestNum):
      smallestNum = list[i]
    if(list[i] > largestNum):
      largestNum = list[i]
    if(list[i] > smallestNum and list[i] < largestNum):
      middleNum = list[i]
  newList.append(smallestNum)
  newList.append(middleNum)
  newList.append(largestNum)
  print(newList)
# sortNumList(myNumList)



