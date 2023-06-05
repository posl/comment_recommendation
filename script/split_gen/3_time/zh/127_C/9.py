def main():
    N, M = map(int, input().split())
    gate = [0] * (N+2)
    for _ in range(M):
        L, R = map(int, input().split())
        gate[L] += 1
        gate[R+1] -= 1
    for i in range(1, N+1):
        gate[i] += gate[i-1]
    print(gate.count(M))
