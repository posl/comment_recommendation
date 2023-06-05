def FizzBuzz(n):
    s = 0
    for i in range(1,n+1):
        if i % 15 == 0:
            s += i
        elif i % 3 == 0:
            s += i
        elif i % 5 == 0:
            s += i
    return s
