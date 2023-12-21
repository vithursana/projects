import json #different imports declared at beginning of code
import requests
import random
import csv
from collections import namedtuple
import datetime


#function with return value
def fetch_random_dog_facts():
    # Fetch a random dog fact
    fact = requests.get("http://dog-api.kinduff.com/api/facts") #API use (1)
    dog_fact_text = fact.text
    facts_json = json.loads(dog_fact_text)

    # Extract the facts from the JSON data
    facts = facts_json.get("facts", [])

    return facts

dream_dogs_list = []  # List to store dream dog entries

print("\nWelcome to the Dog console where you can find out about your favorite dog!\n")

# Boolean use 
while True:
    # Fetch a list of dog breeds and select one randomly
    response = requests.get("https://dog.ceo/api/breeds/list/all") #API use (2)
    data = response.text
    breed_json = json.loads(data)

    # Randomly shuffles the list and prints value
    breeds_list = list(breed_json["message"].keys())
    random.shuffle(breeds_list)
    random_breed = breeds_list[0]
    print("\nYour assigned dog breed is:", random_breed)

    # Fetch and display random dog facts using the function
    facts = fetch_random_dog_facts()
    print("Your dog fact is:")
    print("\n".join(facts))  # Display facts with line breaks

    print("\nWhat is your dream dog?") #Input to save to file
    dream_dog = input()

    print("\nWhat would you call the", dream_dog ,"?") #Input to save to file
    dog_name = input()

    # Get the current date and time as a string
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # String Slicing
    dream_dogs_list.append((dream_dog, dog_name, current_datetime[:11]))

    # Write the user's dream dog to a new file
    with open('Dream_Dogs.txt', 'w') as text_file:
        # Add a header to the file
        text_file.write("Dream Dog,Chosen Name,Date\n")
        # Use a delimiter (e.g., comma) to separate dream_dog, dog_name, and current_datetime with string slicing
        text_file.write(f'{dream_dog},{dog_name},{current_datetime[:11]}\n')  # Add a newline character to separate entries

    # Makes the text easier to read
    with open('Dream_Dogs.txt', 'r') as text_file:
        print("\nContents of 'Dream_Dogs.txt' as a chart:")
        print("Dream Dog".ljust(20), "Chosen Name".ljust(20), "Date".ljust(20))  # Adjust the width as needed
        print("-" * 60)  # Separator
        for line in text_file:
            dream_dog, chosen_name, current_datetime = line.strip().split(',')
            print(dream_dog.ljust(20), chosen_name.ljust(20), current_datetime.ljust(20))  

    # Define the Dog namedtuple
    Dog = namedtuple("dog", "name, min_life_expectancy, max_life_expectancy, max_height_male, max_height_female, max_weight_male, max_weight_female, min_height_male, min_height_female, min_weight_male, min_weight_female, good_with_children, good_with_other_dogs, shedding, grooming")

    # Load dog data from a CSV file
    with open("dog_breeds.csv", "r", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        next(reader)
        dogs = [Dog(*row) for row in reader]

    # Filters dogs based on exact user input
    dream_dog = [dog for dog in dogs if dog.name.lower() == dream_dog.lower()]
    
    # if satement and for function to make sure breed is chosen correctly from list and displayed correctly
    if not dream_dog:
        print("Sorry, no dog breeds match your input:", dream_dog)
        print("\nChoose from this list:")
        for dog in dogs:
            print(dog.name)
    else:
        for dog in dream_dog: # displays information from the CSV file
            print("\nHere are some fascinating insights about", dog.name)
            print("Dog Name:", dog.name)
            print("Maximum Life Expectancy:", dog.max_life_expectancy, "in human years!")
            print("From a scale of 1-5 they are a:", dog.good_with_other_dogs, "with other dogs!")
            print("From a scale of 1-5 they are a:", dog.shedding, "with how much they shed!")

    print("\nDo you want to search for another dog? (yes/no)")
    print("Type no for a quick summary!")
    another_search = input().lower() 
    if another_search != "yes":
        print("Thank you for using running this code!")
        break

# Display the list of dream dogs, their chosen names, and date 
print("\nHere is your summary")
print("\nList of Dream Dogs, Chosen Names, and Date")
print("Dream Dog".ljust(20), "Chosen Name".ljust(20), "Date".ljust(20))  # Header
print("-" * 60)  # Separator
for dream_dog, chosen_name, current_datetime in dream_dogs_list:
    print(dream_dog.ljust(20), chosen_name.ljust(20), current_datetime.ljust(20))  

