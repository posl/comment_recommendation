def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = [int(input()) for _ in range(Q)]
    S = [0] * N
    for a in A:
        S[a-1] += 1
    for l in L:
        print(K - (Q - S[l-1]))
