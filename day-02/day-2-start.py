#Data Types

#String
print("Hello"[0]) #start counting from 0 -> result = "H"
"123" #is a string, cannot use math calculation

#Integer
123

#Float - decimal number
3.14159

#Boolean
True
False

#num_char = len(input("What is your name?"))
#print("Your name has " +numchar + " characters.")
#error will occur as string and int can't be printed together

#print(type(num_char))
#will print the type of data

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
#this will change int into string

a = float(123)
print(type(a))

print(70 + float("100.5"))
#result will be float 170.5

print(str(70)+str(100))
#result will be concatenating 2 string together

print(round(2.666,2))
print(print(8//3)) #"//" will change float into int

result = 4/2
result/=2 #continue calculation

score = 0 #int
height = 1.8 #float
isWinning = True #boolean
#f-string
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

