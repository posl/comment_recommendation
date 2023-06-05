def func(n):
    sum = 0
    for i in range(1,n+1):
        if i % 15 == 0:
            sum += 0
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        else:
            sum += i
    return sum
