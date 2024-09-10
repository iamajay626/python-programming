# print("hello world")
#
# a={''}
# print(type(a))

# 2
# 3 5
# 7 11 13
# 17 19 23 29

# row =5
# for i in range(row):
#     for j in range(i):
#         print(i,end='')
#     print('')
#
# for i in 'inmakes':
#     print(i,end='\n')
#
# num=5
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("7",end=" ")
#     print()
#

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=' ')
#     print()

# d = {n:n*n for n in range(5)}
# print(d)

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def print_prime_pattern(rows, cols):
#     num = 1
#     for i in range(rows):
#         for j in range(cols):
#             while True:
#                 num += 1
#                 if is_prime(num):
#                     print(num, end=" ")
#                     break
#         print()
# print_prime_pattern(5, 5)
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def generate_primes(count):
#     primes = []
#     num = 2
#     while len(primes) < count:
#         if is_prime(num):
#             primes.append(num)
#         num += 1
#     return primes
#
# def print_pattern(rows):
#     primes = generate_primes(rows * (rows + 1) // 2)  # Generate enough primes to cover the pattern
#     num_to_print = 0  # Start from the first prime
#     for i in range(rows):
#         for j in range(i + 1):
#             print(primes[num_to_print], end=" ")
#             num_to_print += 1
#         print()
#
#
# print_pattern(4)

# rows = 4
# num_to_print = 0
# for i in range(rows):
#     for j in range(i + 1):
#         num = num_to_print + 1
#         is_prime = True
#         for k in range(2, int(num ** 0.5) + 1):
#             if num % k == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num, end=" ")
#         num_to_print += 1
#     print()


# rows = 4
# num_to_print = 0
# for i in range(rows):
#     for j in range(i + 1):
#         num = num_to_print + 1
#         is_prime = True
#         for k in range(2, int(num ** 0.5) + 1):
#             if num % k == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num, end=" ")
#         num_to_print += 1
#     print()


# rows = 4
# num_to_print = 0
# for i in range(rows):
#     for j in range(i + 1):
#         num = num_to_print + 1
#         is_prime = True
#         while True:
#             for k in range(2, int(num ** 0.5) + 1):
#                 if num % k == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 print(num, end=" ")
#                 break
#             num += 1
#         num_to_print += 1
#     print()

rows = 4
num_to_print = 2  # Start from the first prime
for i in range(rows):
    next_prime = num_to_print
    for j in range(i + 1):
        print(next_prime, end=" ")
        next_prime += 1
        while True:
            is_prime = True
            for k in range(2, int(next_prime ** 0.5) + 1):
                if next_prime % k == 0:
                    is_prime = False
                    break
            if is_prime:
                break
            next_prime += 1
    num_to_print = next_prime
    print()
