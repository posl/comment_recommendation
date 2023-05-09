def main():
    N, M, Q = map(int, input().split())
    trains = [0] * (N + 1)
    for i in range(M):
        L, R = map(int, input().split())
        trains[L - 1] += 1
        trains[R] -= 1
    for i in range(1, N + 1):
        trains[i] += trains[i - 1]
    for i in range(Q):
        p, q = map(int, input().split())
        print(trains[q] - trains[p - 1])
