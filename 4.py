x = 900
y = 900
lst = []

for i in range(x, 1000):
    for j in range(y, 1000):
        z = str(i*j)
        if len(z) % 2 == 0:
            d = int(len(z)/2)
            part_1 = z[:d]
            part_2 = z[d:]
            if part_1 == part_2[::-1]:
                lst.append(z)

print(max(lst))

#answer = 906609