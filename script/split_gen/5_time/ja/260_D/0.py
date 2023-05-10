def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    stack = []
    for i, p in enumerate(P):
        while len(stack) > 0 and stack[-1][0] > p:
            _, idx = stack.pop()
            ans[idx] = i + 1
        stack.append((p, i))
        if len(stack) >= K:
            _, idx = stack.pop(0)
            ans[idx] = i + 1
    for a in ans:
        print(a)
