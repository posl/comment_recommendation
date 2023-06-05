def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    D = [0] * (10 ** 9 + 2)
    for A, B in AB:
        D[A] += 1
        D[A + B] -= 1
    for i in range(1, 10 ** 9 + 1):
        D[i] += D[i - 1]
    print(*D[1: N + 1])
