
def sortNums(num1, num2, num3):
  newList = []
  if(num3 < num1 and num3 < num2):
    newList.append(num3)
    if(num2 < num1):
        newList.append(num2)
        newList.append(num1)
    if(num1 < num2):
        newList.append(num1)
        newList.append(num2)
  elif(num2 < num1 and num2 < num3):
    newList.append(num2)
    if(num1 < num3):
        newList.append(num1)
        newList.append(num3)
    if(num3 < num1):
        newList.append(num3)
        newList.append(num1)
  elif(num1 < num2 and num1 < num3): 
    newList.append(num1)
    if(num2 < num3):
        newList.append(num2)
        newList.append(num3)
    if(num3 < num2):
        newList.append(num3)
        newList.append(num2)
  print(newList)
  print(type(tuple(newList)))
  print(tuple(newList))
  return tuple(newList)

sortNums(3, 5, 1)