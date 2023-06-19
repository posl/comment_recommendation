def solve():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(0)
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 2):
                if (a[i] - a[j]) * (a[j] - a[k]) == 0 and (a[i] - a[j]) + (a[j] - a[k]) == 0:
                    print("Yes")
                    return
    print("No")
solve()
