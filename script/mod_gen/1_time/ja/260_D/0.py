def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    for i in range(N):
        P[i] -= 1
    stack = [0] * N
    stack[0] = 0
    top = 0
    for i in range(N):
        if P[i] > stack[top]:
            top += 1
            stack[top] = P[i]
        else:
            while top >= 0 and stack[top] >= P[i]:
                ans[stack[top]] = i + 1
                top -= 1
            top += 1
            stack[top] = P[i]
    for i in range(N):
        if ans[i] == -1:
            ans[i] = N + K
    print(*ans, sep='
')

if __name__ == '__main__':
    main()