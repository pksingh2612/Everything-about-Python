from user_defined_function import module
# print(module.factorial_iterative(-1))
# print(module.factorial_recursive(-1))


# # nth fibonacci value
# T = int(input())
# test_cases = [int(input()) for _ in range(T)]

# for number in test_cases:
#     number = number+1
#     print(module.fibonacci_iterative(number))
#     # print(module.fibonacci_recursive(number+1))
#     number = number-1
#     print(module.fibonacci_formula(number)%(1e10+7))


n = int(input())
print(*module.find_all_divisors(n))
# Sort the divisors in ascending order
l = module.find_all_divisors(n)
module.sort_list(module.find_all_divisors(n))
print(*l)

print(module.count_bits(n))


a, b = map(int, input().split())
print(module.count_prime_numbers_between(a, b))
