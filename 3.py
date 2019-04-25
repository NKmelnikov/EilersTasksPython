import itertools


def find_simple(number):
    list1 = []
    for i in range(2, number):
        if number % i == 0:
            if simple(i):
                list1.append(i)
    print(list1)


def simple(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


find_simple(600851475143)
