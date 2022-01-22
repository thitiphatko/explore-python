print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120: #condition
  print("You can ride the rollercoaster.")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Child tickets are $5.") #if condition falls into this, excute first
  elif age<= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y": #add $3 to their bill
    bill = bill + 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow up taller before you can ride.")

# >, <, >=, <=, ==(equal to), !=(inequal to)

#modulo is to divide a number with another number and see the remaining
# 7%3 = 3+3+1 --> 1 is the remaining