def solve():
    s = int(input())
    a = []
    a.append(s)
    for i in range(1, 1000000):
        if a[i-1] % 2 == 0:
            a.append(int(a[i-1]/2))
        else:
            a.append(int(3*a[i-1]+1))
        for j in range(i-1):
            if a[i] == a[j]:
                print(i+1)
                return
solve()
