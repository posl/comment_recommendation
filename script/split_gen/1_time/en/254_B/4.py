def pascal(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1,1]
    else:
        a = pascal(n-1)
        b = [1]
        for i in range(len(a)-1):
            b.append(a[i]+a[i+1])
        b.append(1)
        return b
