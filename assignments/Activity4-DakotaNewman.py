firstName = "Dakota"
lastName = "Newman"
favColor = "Black"
favMeal = "Pizza"

fStringSentence = f"My first name is {firstName}, my last name is {lastName}, my favorite color is {favColor}, my favorite meal is {favMeal}"

print(fStringSentence)

concattedSentence = "My first name is " + firstName, "My last name is " + lastName, "My favorite color is " + favColor, "and my favorite meal is " + favMeal + "."

print(concattedSentence)

argumentByPositionSentence = "My first name is {0}, my last name is {1}, my favorite color is {2}, and my favorite meal is {3}".format("Dakota", "Newman", "Black", "Pizza")

print(argumentByPositionSentence)

argumentByNameSentence = "My first name is {firstName}, my last name is {lastName}, my favorite color is {favColor}, and my favorite meal is {favMeal}".format(firstName = "Dakota", lastName = "Newman", favColor = "Black", favMeal = "Pizza")

print(argumentByNameSentence)
