# Activity 9.3
# Write a function called isSorted which will be passed in as a list of numbers
# Your functions job is to determine if the list in the need of being sorted, or if it already came sorted
# Your function should return a boolean determining whether or not that is the case

sortedList = [1, 4, 5, 6, 7]
unsortedList = [83, 23, 198, 84]

def isSorted(list):
  count = 0
  for i in range(len(list)):
    if(list[i] < list[i + 1]):
      print(list[i])
      count += 1
      if (count == len(list) -1):
        print("This list is sorted already")
        return True
    else:
      print("This list needs sorted")
      return False

isSorted(sortedList)
isSorted(unsortedList)