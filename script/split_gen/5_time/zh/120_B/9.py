def func(a,b,k):
    count = 0
    for i in range(1,101):
        if a%i==0 and b%i==0:
            count += 1
            if count == k:
                return i
