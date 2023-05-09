def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(Q)]
    A.sort()
    for i in range(Q):
        ans = 0
        for j in range(N):
            if A[j] >= x[i]:
                ans = N - j
                break
        print(ans)
