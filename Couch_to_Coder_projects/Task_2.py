rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]

for river in rivers:
    print( river["name"])


total = 0
for river in rivers:
    total += river["length"]
print(total, "This is the total")

for river in rivers:
      if river["name"][0]== "M":
         print(f"{river['name']}")
          
counter = 0
for river in rivers:
    totals = river["length"]
    print(river["name"], "in km is", totals*1.6)


#Task 2
# 1. In a for loop, print out each river's name!
# 2. In another for loop, add up and print out the total length of all the rivers!

#extenion
# 1. Print out every river's name that begins with the letter M !
# 2. The length of the rivers are in miles. Print out every river's length in kilometres! (1 mile is
# roughly 1.6 km)


      