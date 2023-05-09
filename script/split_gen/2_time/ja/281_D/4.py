def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    max = 0
    for i in range(0, N-K+1):
        if A[i+K-1] - A[i] > max:
            max = A[i+K-1] - A[i]
    if max > D:
        print(-1)
    else:
        print(max)
