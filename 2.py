a = 1
b = 2
s = 2
while a + b < 4000000:
    a, b = b, a + b
    if (a + b) % 2 == 0:
        s += a + b
print(s)

#answer = 4613732