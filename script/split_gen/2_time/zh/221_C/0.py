def solve():
    n = int(input())
    ans = 0
    l = len(str(n))
    if l == 2:
        print(1)
        return
    for i in range(1, l):
        a = int(str(n)[:i])
        b = int(str(n)[i:])
        ans = max(ans, a * b)
    print(ans)
