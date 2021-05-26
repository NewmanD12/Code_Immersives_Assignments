import random

# Activity 10.1 Create a list of random numbers using getrandbits
def listOfRandomNums(num):
  listOfNums = []
  for i in range(num):
    randomNum = random.getrandbits(10)
    listOfNums.append(randomNum)
  return listOfNums

result = listOfRandomNums(15)
result2 = listOfRandomNums(1000)

# print(result)
# print(result2)

# Activity 10.2 create a function that will generate a random list, with the values passed in between 20-40

def listOfRandomNums2(num):
  listOfNums = []
  for i in range(num):
    randomNum = random.randrange(20, 40)
    listOfNums.append(randomNum)
  return listOfNums

result3 = listOfRandomNums2(15)
result4 = listOfRandomNums2(12)

print(result3)
print(result4)




