programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary["Bug"]) #inside [] is the key to find in the dictionary

#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

#create an empty disctionary.
empty_dictionary = {}

#wipe an existing empty_dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print (key)
    print(programming_dictionary[key])

##########

#Nesting 
Capitals = {
    "France", "Paris",
    "Germany", "Berlin",
}

#Nesting a list in a dictionary
travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"]}, "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburn", "Stuttgart"]}, "total_visits": 5},
}

#Nesting a disctionary in a dictionary
travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"]}, "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburn", "Stuttgart"]}, "total_visits": 5},
}

#Nesting dictionary in a list
travel_log = [
    {
        "country": "France", #string
        "cities_visited":["Paris", "Lille", "Dijon"], #list
        "total_visits": 12 #integer
    },
    {
        "country": "Germany", 
        "cities_visited":["Berlin", "Hamburn", "Stuttgart"], 
        "total_visits": 5
    },
]