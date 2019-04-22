def find_simple(number):
    for i in range(1, number+1):
        if number % i == 0:
            continue
        print(i)


find_simple(10)
