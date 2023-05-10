def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    P = [K - Q] * N
    for a in A:
        P[a - 1] += 1
    for p in P:
        if p > 0:
            print("Yes")
        else:
            print("No")
