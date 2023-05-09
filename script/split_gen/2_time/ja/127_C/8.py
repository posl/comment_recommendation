def main():
    N, M = map(int, input().split())
    # 1-indexed
    gates = [0] * (N + 1)
    for _ in range(M):
        L, R = map(int, input().split())
        gates[L] += 1
        gates[R + 1] -= 1
    for i in range(1, N + 1):
        gates[i] += gates[i - 1]
    print(gates.count(M))
