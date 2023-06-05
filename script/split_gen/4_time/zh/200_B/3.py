def func(n, k):
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    return n
print(func(2021, 4))
print(func(40000, 2))
print(func(8691, 20))
