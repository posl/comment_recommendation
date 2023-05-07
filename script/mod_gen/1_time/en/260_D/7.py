def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [x - 1 for x in P]
    ans = [-1] * N
    stack = []
    for i in range(N):
        while stack and P[stack[-1]] < P[i]:
            stack.pop()
        if stack and i - stack[-1] == K:
            ans[stack[-1]] = i
            stack.pop()
        stack.append(i)
    for i in range(N):
        if ans[i] == -1:
            ans[i] = N
    for i in range(N - 1):
        ans[i] = min(ans[i], ans[i + 1])
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()