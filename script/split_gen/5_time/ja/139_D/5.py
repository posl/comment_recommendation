def solve():
    N = int(input())
    ans = 0
    if N == 1:
        print(0)
        return
    if N % 2 == 0:
        ans = N // 2 * (N - 1)
    else:
        ans = (N - 1) // 2 * N
    print(ans)
