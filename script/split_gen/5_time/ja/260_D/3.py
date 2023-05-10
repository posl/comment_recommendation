def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    result = [-1] * N
    stack = []
    for i in range(N):
        while len(stack) > 0 and P[stack[-1]] >= P[i]:
            stack.pop()
        if len(stack) > 0:
            result[i] = stack[-1] + 1
        stack.append(i)
        if len(stack) >= K:
            stack.pop(0)
    for i in range(N):
        print(result[i])
