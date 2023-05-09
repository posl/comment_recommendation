def main():
    import sys
    from itertools import accumulate
    readline = sys.stdin.readline
    read = sys.stdin.read
    N, *A = map(int, read().split())
    A = [0] + A
    A = list(accumulate(A))
    ans = 10**9
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                ans = min(ans, max(A[i], A[j]-A[i], A[k]-A[j], A[N]-A[k])-min(A[i], A[j]-A[i], A[k]-A[j], A[N]-A[k]))
    print(ans)
