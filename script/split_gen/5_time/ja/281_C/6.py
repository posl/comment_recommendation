def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    N,T = map(int,readline().split())
    A = list(map(int,readline().split()))
    sumA = sum(A)
    cnt = T//sumA
    T -= cnt*sumA
    cumsum = [0]*(N+1)
    for i in range(N):
        cumsum[i+1] = cumsum[i]+A[i]
    for i in range(N):
        if T > cumsum[i] and T <= cumsum[i+1]:
            print(i+1,T-cumsum[i])
            break
    return
