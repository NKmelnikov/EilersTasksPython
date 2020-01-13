lst = []


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


for a in range(2, 2000000):
    if is_prime(a):
        lst.append(a)

print(sum(lst)) #142913828922
