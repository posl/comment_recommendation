def f(x):
    if x == 1:
        return 1
    else:
        sum = 1
        for i in range(2, x+1):
            if x % i == 0:
                sum += i
        return sum
