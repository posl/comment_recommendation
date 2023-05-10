def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = [0 for _ in range(N+1)]
    for i in range(N):
        B[i+1] = B[i] + A[i]
    import collections
    C = collections.deque()
    ans = 0
    for i in range(N+1):
        while C and B[C[-1]] >= B[i]:
            C.pop()
        C.append(i)
        if i >= M:
            if C[0] == i - M:
                C.popleft()
            ans = max(ans, B[i] - B[C[0]])
    print(ans)
