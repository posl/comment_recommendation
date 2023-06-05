def f(n,a,b):
    count = 0
    for i in range(1,n+1):
        if i%a != 0 and i%b != 0:
            count += i
    return count
