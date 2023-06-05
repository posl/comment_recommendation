def solve():
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i],y[i] = map(int,input().split())
    s = input()
    if s[0] == 'R':
        for i in range(n):
            x[i] = -x[i]
    if s[-1] == 'L':
        for i in range(n):
            x[i] = -x[i]
    for i in range(n):
        if s[i] == 'R':
            x[i] = x[i] + 1
        else:
            x[i] = x[i] - 1
    for i in range(n-1):
        for j in range(i+1,n):
            if x[i] == x[j] and y[i] == y[j]:
                print('Yes')
                return
    print('No')
