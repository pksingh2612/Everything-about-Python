def fahrenheit_to(celsius):
    return (celsius * 9/5) + 32

def celsius_to(fahrenheit):
    return (fahrenheit - 32) * 5/9

def Sum(numbers):
    return sum(numbers)

def is_even(number):
    return number%2==0

def is_odd(number):
    return number%2==1

def sum_even(numbers):
    result = 0
    for number in numbers:
        if is_even(number):
            result += number
    return result

def sum_odd(numbers):
    result = 0
    for number in numbers:
        if is_odd(number):
            result += number
    return result

def factorial_recursive(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif number in [0, 1]:
        return 1
    else:
        return number * factorial_recursive(number - 1)
    
def factorial_iterative(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    else:
        result = 1
        for i in range(1, number+1):
            result *= i
        return result

def fibonacci_iterative(number):
    if number < 0:
        raise ValueError("Invalid input. n should be a positive integer.")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    
    prev_1 = 0
    prev_2 = 1
    fibonacci_number = None

    for _ in range(2, number):
        fibonacci_number = prev_1 + prev_2
        prev_1, prev_2 = prev_2, fibonacci_number

    return fibonacci_number