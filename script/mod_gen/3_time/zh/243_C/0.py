def solution():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    s = input()
    #print(x, y, s)
    for i in range(n-1):
        for j in range(i+1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print("Yes")
                return
    for i in range(n-1):
        for j in range(i+1, n):
            if x[i] > x[j] and s[i] == 'R' and s[j] == 'L':
                print("Yes")
                return
            if x[i] < x[j] and s[i] == 'L' and s[j] == 'R':
                print("Yes")
                return
    print("No")
solution()
