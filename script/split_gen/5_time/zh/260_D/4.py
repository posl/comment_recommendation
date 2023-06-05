def solve():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    ans = [-1]*N
    stack = []
    for i in range(N):
        while stack and stack[-1][0] >= P[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1][1]
        stack.append((P[i],i+1))
    for i in range(K):
        print(ans[i])
