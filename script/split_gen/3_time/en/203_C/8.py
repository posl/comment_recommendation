def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # print(N, K)
    # print(A)
    # print(B)
    # print()
    d = defaultdict(int)
    for i in range(N):
        d[A[i]] += B[i]
    # print(d)
    # pr
