def solve():
    N = int(input())
    S = list(map(int, input().split()))
    A = []
    for i in range(N):
        if i == 0:
            A.append(S[i])
        else:
            A.append(S[i] - S[i-1])
    print(*A)
solve()
