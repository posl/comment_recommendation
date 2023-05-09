def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    good = [True] * N
    for i in range(M):
        if H[A[i]] >= H[B[i]]:
            good[B[i]] = False
        if H[A[i]] <= H[B[i]]:
            good[A[i]] = False
    print(sum(good))
