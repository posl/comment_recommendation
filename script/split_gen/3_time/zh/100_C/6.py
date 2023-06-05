def solve(n, a):
    #print(n)
    #print(a)
    count = 0
    for i in range(n):
        while a[i]%2 == 0:
            a[i] = a[i]/2
            count += 1
    return count
