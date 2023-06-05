def solve():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    ans = [True] * N
    for a in A:
        ans[a-1] = not ans[a-1]
    for i in range(N):
        if ans[i]:
            print("Yes")
        else:
            print("No")
