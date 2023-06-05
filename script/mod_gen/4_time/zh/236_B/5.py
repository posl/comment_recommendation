def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    for i in range(0, 4*n, 2):
        if a[i] != a[i+1]:
            print(a[i])
            break
solve()
