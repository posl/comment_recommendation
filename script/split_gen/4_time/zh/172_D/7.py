def f(x):
    sum = 0
    for i in range(1,x+1):
        if x % i == 0:
            sum += 1
    return sum
