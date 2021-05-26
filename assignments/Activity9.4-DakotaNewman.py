# Write a function to determine if a given string will return a boolean determining whether or not that string is a Palindrome. 

def isPalindrome(str):
  str = str.replace(" ", "")
  str = str.lower()
  reversedString = ""
  for i in range(1, len(str) + 1):
      reversedString += str[len(str) - i]
  # print(reversedString)
  if(str == reversedString):
    print("This is a palidrome")
    return True
  else:
    print("This is not a palidrome")
    return False

isPalindrome("racecar")
isPalindrome("notracecar")