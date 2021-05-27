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
  print(updatedList)
  return updatedList

# standardDeviation(grades)
# standardDeviation(grades2)

# Activity 11.2
# Write an average value of the curved exam grades.
  # 1. The curved exam grades is the solution you made for activity 11.1
  # 2. This means you can reference you own functino if need be


def findAverage(list):
  average = statistics.mean(list)
  print(average)
  return average

# findAverage(standardDeviation(grades))
findAverage(standardDeviation(grades2))
findAverage(standardDeviation(grades3))
# findAverage(standardDeviation(grades4))