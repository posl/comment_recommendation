def problem274_d():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.insert(0, 0)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 2):
            if i == j:
                continue
            if a[i] + a[j] <= abs(x - y):
                print("Yes")
                return
    print("No")
    return
problem274_d()
