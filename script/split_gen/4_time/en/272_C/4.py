def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        for i in range(n-1):
            if a[i] % 2 == 0 and a[i] + 1 == a[i+1]:
                print(a[-1])
                break
        else:
            print(-1)
solve()
