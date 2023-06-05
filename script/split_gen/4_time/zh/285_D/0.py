def solve():
    N = int(input())
    S = [None] * N
    T = [None] * N
    for i in range(N):
        S[i],T[i] = input().split()
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i] == T[j]:
                print("No")
                return
    print("Yes")
solve()
