def solve():
    N = input()
    ans = 0
    for i in range(1, len(N)):
        A = int(N[:i])
        B = int(N[i:])
        ans = max(ans, A * B)
    print(ans)
