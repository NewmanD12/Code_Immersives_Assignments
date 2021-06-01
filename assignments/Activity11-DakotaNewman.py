import statistics

# Activity 11.1
# Given a list of exam grades represented by Numbers/Integers; calculate the standard deviation of the exam greades represented by some numeric data set.
# Return a list with all of the exam values updated by itself Plus the standard deviation
# Include something that staes that if adding the standard deviation to the current exam score goes above 100, then I will simply pass the 100 right back into the list at that particular index, and for everything else, just add the standard deviation normally to the current exam score

grades = [100, 85, 85, 75, 75, 75, 65, 65, 50, 50]
grades2 = [100, 23, 53, 65, 100, 82, 94, 28, 19, 38]
grades3 = [1, 2, 3, 4, 5]
grades4 = [1, 2, 3]

def standardDeviation(list):
  updatedList = []
  deviation = statistics.stdev(list)
  # print(deviation)
  for i in range(len(list)):
    if(list[i] + deviation < 100):
      updatedGrade = int(list[i] + deviation)
      updatedList.append(updatedGrade)
    if(list[i] + deviation >= 100):
      updatedList.append(100)
  # print(updatedList)
  return updatedList

# standardDeviation(grades)
# standardDeviation(grades2)

# Activity 11.2
# Write an average value of the curved exam grades.
  # 1. The curved exam grades is the solution you made for activity 11.1
  # 2. This means you can reference you own functino if need be


def findAverage(list):
  average = statistics.mean(standardDeviation(list))
  print(average)
  return average

# findAverage(grades)
# findAverage(grades2)
# findAverage(grades3)
# findAverage(grades4)


# Activity 11.3
# Create a function that given a list of numbers will return to me a list of booleans
# Your function will take in a list of numbers, and if the values are less than 55 exclusive, then you substitue that list item with a "False". For all others, substitute the current list item value to "True".
# Return to me that list, and before returning, check its type (it should be a list)


randomList = [23, 55, 54, 75, 97, 48, 92, 83]


def lessThan55(list):
  for i in range(len(list)):
    if(list[i] < 55):
      list[i] = False
    else: 
      list[i] = True

  print(list)
  print(type(list))
  return list


# lessThan55(randomList)


# Activity 11.4
# now I would like to have a function that takes a list and tells me how many people passed the class
# I would like you to do this with a given list of 'grades'
# given a list of integers represeting exam grades(whether they are curved or not), print a message telling me how many people passed or failed the class base on the fact that 55+  is passing and below is failing. 

# call the function "Class Report"


# grades = [100, 85, 85, 75, 75, 75, 65, 65, 50, 50]

def classReport(list):
  passed = 0
  failed = 0
  for i in range(len(list)):
    if(list[i] < 55):
      failed += 1
    elif(list[i] >= 55):
      passed += 1
  
  print(f"{passed} is how many kids passed, {failed} is how many kids failed")

# classReport(grades)
# classReport(standardDeviation(grades))