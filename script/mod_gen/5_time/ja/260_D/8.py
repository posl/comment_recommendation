def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    A = [0] * N
    for i in range(N):
        A[P[i] - 1] = i + 1
    ans = [-1] * N
    stack = []
    for i in range(N):
        if len(stack) == 0:
            stack.append(A[i])
            continue
        if stack[-1] < A[i]:
            stack.append(A[i])
            continue
        if len(stack) == K:
            for j in range(K):
                ans[stack[j] - 1] = i + 1
            stack = []
            continue
        if stack[-1] > A[i]:
            stack.append(A[i])
            continue
    for i in range(len(stack)):
        ans[stack[i] - 1] = N
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()