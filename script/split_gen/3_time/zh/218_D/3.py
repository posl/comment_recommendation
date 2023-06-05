def solve():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = [int(_) for _ in input().split()]
        x.append(x_i)
        y.append(y_i)
    x.sort()
    y.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if x[i] < x[j] and y[i] < y[j]:
                if x[i] in x and x[j] in x and y[i] in y and y[j] in y:
                    ans += 1
    print(ans)
