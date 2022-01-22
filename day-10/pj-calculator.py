from art import logo
print(logo)

#add
def add(n1, n2):
    return n1 + n2
#subtract
def subtract(n1, n2):
    return n1 - n2
#multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1, n2):
    return n1 / n2

opertaions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is the first number?: "))
for symbol in opertaions:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What is the second number?: "))
calculation_function = opertaions[operation_symbol]
answer = calculation_function(num1, num2)



print(f"{num1} {operation_symbol} {num2} = {answer}")