def main():
    import sys
    from io import StringIO
    import unittest
    def resolve():
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        A.sort()
        for i in range(N):
            if K <= A[i]:
                print(K)
                K = 0
            else:
                print(A[i])
                K -= A[i]
        for i in range(N):
            print(K // (N - i), end=' ')
            K -= K // (N - i)
    # -----------------------------
    if sys.argv[-1] == 'ONLINE_JUDGE':
        resolve()
    else:
        sys.stdin = StringIO("""\
2 7
1 8
        """)
        unittest.main()
