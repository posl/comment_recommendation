def main():
    N = int(input())
    P = [int(p) for p in input().split()]
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(" ".join(str(q) for q in Q))
