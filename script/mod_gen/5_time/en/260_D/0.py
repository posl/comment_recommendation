def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    stack = []
    for i in range(N):
        p = P[i]
        while stack and stack[-1][0] < p:
            _, j = stack.pop()
            ans[j] = i + 1
        stack.append((p, i))
        if len(stack) == K:
            _, j = stack.pop(0)
            ans[j] = i + 1
    print('\n'.join(map(str, ans)))
solve()

if __name__ == '__main__':
    solve()