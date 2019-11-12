#my solution

def divider(n):
    d = []
    g = []
    for i in range(1, 20):
        if n % i == 0:
            d.append(1)
        else:
            d.append(0)

    if 0 not in d:
        g.append(n)
        return g

    return False


def check():
    for i in range(100000000, 1000000000):
        if divider(i):
            print(divider(i))

check()

# answer = 232792560

#alternative solution
i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print(i)