def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [0 for i in range(N)]
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(*Q)
