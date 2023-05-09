def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if sum(A) <= 0:
        print(0)
        return
    ans = 0
    for a in A:
        ans += a
        if ans < 0:
            print(0)
            return
    print(ans)
