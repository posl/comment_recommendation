def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = -1
    stack = []
    for i in range(n):
        while len(stack) > 0 and stack[-1][0] >= p[i]:
            stack.pop()
        if len(stack) > 0:
            ans[i] = stack[-1][1]
        stack.append((p[i], i+1))
        if len(stack) == k:
            stack.pop(0)
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()