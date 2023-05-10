def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    result = [-1] * N
    stack = []
    for i in range(N):
        if len(stack) == 0:
            stack.append(P[i])
        else:
            if P[i] > stack[-1]:
                stack.append(P[i])
            else:
                while len(stack) > 0 and stack[-1] >= P[i]:
                    stack.pop()
                stack.append(P[i])
        if len(stack) == K:
            for j in range(K):
                result[stack[-1] - 1] = i + 1
                stack.pop()
    for i in range(N):
        print(result[i])

if __name__ == '__main__':
    main()