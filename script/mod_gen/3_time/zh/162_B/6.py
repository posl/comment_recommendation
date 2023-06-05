def fizzbuzz(n):
    s = 0
    for i in range(1,n+1):
        if i % 15 == 0:
            s += 0
        elif i % 3 == 0:
            s += 0
        elif i % 5 == 0:
            s += 0
        else:
            s += i
    return s
n = int(input())
print(fizzbuzz(n))
