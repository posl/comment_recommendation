def main():
    import sys
    import bisect
    def input(): return sys.stdin.readline().rstrip()
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    # A[i] * A[j] < A[k] * A[l] となる組み合わせの数を求める
    def count(a, b):
        if a == b:
            return N - a
        elif a < b:
            return bisect.bisect_left(A, (A[K] + A[a] - 1) // A[a]) - b
        else:
            return bisect.bisect_left(A, (A[K] + A[b] - 1) // A[b]) - a
    ans = 0
    for i in range(N):
        for j in range(i + 1, N + 1):
            ans += count(i, j)
    print(ans)
