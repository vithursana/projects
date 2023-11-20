import csv
from collections import namedtuple


car = namedtuple("car", "model, year,price,transmission,mileage,fuelType,tax,mpg,engineSize" )


with open("task_4_data.csv", "r",encoding="utf8") as csvfile:
   reader = csv.reader(csvfile, skipinitialspace= True)
   next(reader)
   cars = [car(*row) for row in reader]

#1. What is the most expensive VW car listed?
   most_expensive_car = cars[0]

   for car in cars:
      if(int(car.price)> int(most_expensive_car.price)):
         most_expensive_car= car
print("Most expensive car is ", most_expensive_car)


golf_car =[car for car in cars if "Golf" in car.model]

print(golf_car)

#2. Find all the VW Golf models. What is their average price?

golf_model = 0
car_total = 0
for car in cars:
   if (car.model == "Golf"):
      golf_model += 1
      car_total += int(car.price)

Average= car_total/golf_model

print(Average)

#3. What is the average milage for VW Polo models registered in 2020?
golf_model2 = 0
mileage= 0
for car in cars:
   if (car.model == "Golf" and car.year =="2020"):
      golf_model2 += 1
      mileage += int(car.mileage)

Average2= mileage/golf_model2

print(Average2)