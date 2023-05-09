def main():
    # input
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # compute
    d = [0] * N
    for i in range(N-1):
        d[i] = A[i+1] - A[i]
    d[N-1] = K - A[N-1] + A[0]
    d.sort()
    ans = 0
    for i in range(N-1):
        ans += d[i]
    # output
    print(ans)
