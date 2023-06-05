def f(n,d):
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key=lambda x:x[0])
    r = 0
    for i in range(n):
        if i == 0:
            r += (l[i][1] - l[i][0]) // d + 1
        else:
            if l[i][0] <= l[i - 1][1]:
                r += (l[i][1] - l[i - 1][1]) // d
                if (l[i][1] - l[i - 1][1]) % d == 0:
                    r -= 1
            else:
                r += (l[i][1] - l[i][0]) // d + 1
    print(r)
n,d = map(int,input().split())
f(n,d)
