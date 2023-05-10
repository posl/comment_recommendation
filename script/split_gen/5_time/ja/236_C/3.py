def solve():
    N,M = map(int,input().split())
    S = input().split()
    T = input().split()
    ans = []
    for i in range(N):
        if S[i] in T:
            ans.append("Yes")
        else:
            ans.append("No")
    for i in range(N):
        print(ans[i])
    return 0
