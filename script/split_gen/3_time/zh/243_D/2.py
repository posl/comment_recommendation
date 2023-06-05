def solve():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == "U":
            ans //= 2
        elif S[i] == "L":
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    print(ans)
solve()
