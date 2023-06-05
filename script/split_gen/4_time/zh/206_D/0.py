def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    s = set()
    for i in range(n):
        if a[i] in s:
            ans += 1
            s.remove(a[i])
        else:
            s.add(a[i])
    print(ans)
