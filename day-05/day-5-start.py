#for loop with list
fruits = ["Apple","Peach","Pear"]
for fruit in fruits: #assign each item in the list to "fruit" one by one
  print(fruit)
  print(fruit + " Pie")
  #all indented lines are under for loop
print(fruits)

# for loop with range
for number in range(1,11,3): #(start, end-1, step)
  print(number)

#sum of 1 - 100
total = 0
for number in range (1,101):
  total = total + number
print(total)