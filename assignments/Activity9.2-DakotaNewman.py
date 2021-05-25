# Activity 9.2 
# Given a list of any size of numbers, return the max number in that list
myBiggerNumList = [343, 342343,534,6,3736734567, 8372849, 843794, 775738, 8237476457, 837262]

def findMax(list):
  maxNum = list[0]
  for i in range(len(list)):
    if(list[i] > maxNum):
      maxNum = list[i]
  print(maxNum)

# findMax(myNumList)
# findMax(myBiggerNumList)