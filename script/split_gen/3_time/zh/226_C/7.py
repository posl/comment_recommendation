def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
        A[i] = [a - 1 for a in A[i]]
    from collections import deque
    q = deque()
    for i in range(N):
        if K[i] == 0:
            q.append(i)
    dp = [0] * N
    while q:
        i = q.popleft()
        if A[i]:
            dp[i] = max(dp[j] for j in A[i]) + T[i]
        else:
            dp[i] = T[i]
        for j in range(N):
            if j in A[i]:
                A[j].remove(j)
                if not A[j]:
                    q.append(j)
    print(max(dp))
