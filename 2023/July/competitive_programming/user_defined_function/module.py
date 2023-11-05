import math

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

def fibonacci_iterative(n): 
    # dynamic programming space optimized & matrix exponentiation
    M = 1e9 + 7
    prev_1 = 0
    prev_2 = 1
    if n <= 0:
        raise ValueError("Invalid input. Number should be a positive integer.")
    elif n == 1:
        return prev_1
    elif n == 2:
        return prev_2
    else:
        for _ in range(2, n):
            prev_1, prev_2 = prev_2, prev_1 + prev_2
            prev_2 = prev_2 % M
            prev_2 = int(prev_2)
        return prev_2
    
def fibonacci_recursive(n):
    if n <= 0:
        raise ValueError("Invalid input. Number should be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_formula(n):
    sqrt_5 = math.sqrt(5)
    return (((1+sqrt_5)**n)-((1-sqrt_5))**n)/(2**n*sqrt_5)

def find_all_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid duplicates for perfect squares
                divisors.append(n // i)
    return divisors

def sort_list(l):
    return l.sort()

def decimal_to_binary(decimal):
    binary = ''
    
    if decimal == 0:
        binary = '0'
    
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    
    return binary

def count_bits(n):
    count = 0
    while n > 0:
        # bitwise AND operation (n & 1) to check the least significant bit of n
        # If the result is 1, we increment the count variable
        count += n & 1 
        # we shift n one bit to the right (n >>= 1) to discard the least significant bit
        n >>= 1
    return count

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_numbers_between(a, b):
    count = 0
    for num in range(a, b + 1):
        if is_prime(num):
            count += 1
    return count

def reverse(l):
    return l[:,:,-1]
