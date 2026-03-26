# 1 Max of three
def max_three(a, b, c):
    return max(a, b, c)

# 2 Sum list
def sum_list(lst):
    return sum(lst)

# 3 Multiply list
def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result

# 4 Reverse string
def reverse_string(s):
    return s[::-1]

# 5 Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# 6 Range check
def in_range(n, start, end):
    return start <= n <= end

# 7 Count upper/lower
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# 8 Unique list
def unique_list(lst):
    return list(set(lst))

# 9 Prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 10 Even numbers
def even_list(lst):
    return [x for x in lst if x % 2 == 0]

# 11 Perfect number
def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

# 12 Palindrome
def is_palindrome(s):
    return s == s[::-1]