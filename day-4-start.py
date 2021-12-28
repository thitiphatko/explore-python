import random
# import my_module #import data from other file

randomInteger = random.randint(1, 10) #including starting and ending numbers
print(randomInteger)

# print(my_module.pi) #print data from other file

randomFloat = random.random() #random float between (0,1) not including 1 (0.00-0.99)
print(randomFloat)

randomFloat1 = random.random()* 5 #0.00-4.99
print(randomFloat1)

#list - store in order
states_of_america = ["Delaware","Pennsylvaniaaa", "New Jersey"]
print(states_of_america[1])
print(states_of_america[-1]) #count from the last item
states_of_america[1] = "Pennsylvania" #change item in the list
states_of_america.append("Georgia") #add new item into the last order
states_of_america.extend(["Connecticut","Massachusetts","Maryland"])

num_of_states = len(states_of_america)
print(states_of_america[num_of_states-1])

# dirty_dozen = ["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]
#want to seperate between fruits and vegetables

fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]
dirty_dozen = [fruits,vegetables]
print(dirty_dozen)

print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2]) #[1] = select first list(vegetables) and select 2nd item in the list(tomatoes)
