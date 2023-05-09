def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    stack = []
    for i in range(N):
        while stack and stack[-1][0] < P[i]:
            ans[stack.pop()[1]] = i + 1
        stack.append((P[i], i))
    while stack:
        ans[stack.pop()[1]] = N + K
    for i in range(N):
        print(ans[i])
