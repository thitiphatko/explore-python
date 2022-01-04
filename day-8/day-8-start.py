# Create a function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet()

# Function that allos for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
greet_with_name("Joe")
# Function is a parameter. Input is an argument.

# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}.")
greet_with(location = "UK", name = "Joe")

# def my_function(a,b,c): positional arguments
#     a = 1, b = 2, c = 3

# def my_function( a = 1, b = 2, c = 3 ): keyword arguments