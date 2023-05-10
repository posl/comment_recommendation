def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = [int(input()) for _ in range(Q)]
    P = [0] * N
    for a in A:
        P[a-1] += 1
    for l in L:
        print(K - (Q - P[l-1]))
