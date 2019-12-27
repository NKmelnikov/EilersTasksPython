k = 0
for i in range(1, 101):
    k += i ** 2
l = 0
for j in range(1, 101):
    l += j
l = l**2
r=l-k
print(r)

#answer = 25164150
#sum([x for x in range(101)])**2 - sum([x**2 for x in range(101)])