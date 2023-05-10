def myCode():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(1, n):
        if a[i] % a[0] != 0:
            ans += 1
    print(ans)
