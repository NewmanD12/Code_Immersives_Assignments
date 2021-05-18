car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Access the dictionary to print the value of the "model" of the car. 
model = car.get('model')
print(model)

# copy method
copiedCar = car.copy()
#expect dictionary exactly like original
print(copiedCar)
# got dictionary as expected

# get method gets the value for the key you passed as an arguement
getYear = car.get('year')
#expect 1964
print(getYear)
#got 1964

# pop method
#it will remove the model and the value from the dictionary
popMethod = car.pop('model')
print(car) 
# it removed the model

#popitem method
# it will removed the last item in the dictionary
popItemMethod = car.popitem()
print(car)

#clear method
# it will clear the entire dictionary
clearedDict = car.clear()
print(clearedDict)

#update method
# it will allow you to update the specified key/value pair
car.update({'model' : 'Pinto'})
print(car)
