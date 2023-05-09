def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    stack = []
    for i in range(N):
        p = P[i]
        while stack and stack[-1][0] < p:
            stack.pop()
        stack.append((p, i))
        if len(stack) == K:
            ans[stack[0][1]] = i + 1
            stack = stack[1:]
    for i in range(N):
        p = P[i]
        if ans[p - 1] == -1:
            ans[p - 1] = N
    print('
'.join(list(map(str, ans))))

if __name__ == '__main__':
    main()