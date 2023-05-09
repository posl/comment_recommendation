def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    w = [0] * (W+1)
    for i in range(N):
        for j in range(W, A[i]-1, -1):
            w[j] = max(w[j], w[j-A[i]] + A[i])
    print(w.count(W))
