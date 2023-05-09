def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    stack = []
    for i in range(n):
        x = p[i]
        while stack and stack[-1][0] >= x:
            stack.pop()
        if stack:
            ans[i] = stack[-1][1]
        stack.append((x, i + 1))
        if len(stack) == k:
            stack = []
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()