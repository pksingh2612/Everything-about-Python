# Creating a Global Variable 
my_variable = "Hello, world!"

# Access the global variable in the top-level segment
def my_function():
    print(my_variable)

# Acccess this global variable outside
if __name__ == '__main__':
    print(my_variable)  # Access the global variable in the top-level segment
    my_function()