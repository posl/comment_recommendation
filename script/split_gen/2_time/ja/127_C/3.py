def main():
    N, M = map(int, input().split())
    gates = [0] * N
    for i in range(M):
        L, R = map(int, input().split())
        gates[L-1] += 1
        if R < N:
            gates[R] -= 1
    for i in range(1, N):
        gates[i] += gates[i-1]
    print(gates.count(M))
