def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    for i in range(N - 1):
        print(Q[i], end = " ")
    print(Q[N - 1])
