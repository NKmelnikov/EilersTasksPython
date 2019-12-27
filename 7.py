def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


lst = []

for i in range(1, 1000000):
    if is_prime(i):
        lst.append(i)

print(lst[10001])

#answer 104743

#better solution
# start = 3
# index=1
# while True:
#   if is_prime(start) == True:
#         index+=1
#   if index == 10001:
#         print(start)
#         break
#   start+=2