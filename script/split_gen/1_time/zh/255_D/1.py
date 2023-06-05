def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    A.append(0)
    for i in range(N):
        A[i+1] += A[i]
    for x in X:
        idx = bisect.bisect_left(A, x)
        ans = 0
        if idx == N:
            ans = x - A[N-1] + N
        elif A[idx] == x:
            ans = x - A[idx-1]
        else:
            ans = x - A[idx-1] + N - idx
        print(ans)
