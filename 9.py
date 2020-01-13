import numpy

array = []
for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 500):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                array.append([a, b, c])


print(numpy.prod(array[0])) #31875000
print(array[0]) #200, 375, 425
