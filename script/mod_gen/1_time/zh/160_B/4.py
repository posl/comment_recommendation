def problem160_b(x):
    #x = int(input())
    if x >= 500:
        a = x // 500
        b = x % 500
        if b >= 5:
            c = b // 5
            d = b % 5
            return a * 1000 + c * 5
        else:
            return a * 1000
    else:
        if x >= 5:
            c = x // 5
            d = x % 5
            return c * 5
        else:
            return 0
print(problem160_b(1024))
print(problem160_b(0))
print(problem160_b(1000000000))
