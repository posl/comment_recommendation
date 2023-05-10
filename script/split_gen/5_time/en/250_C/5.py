def main():
    N, Q = [int(x) for x in input().split()]
    a = [int(input()) for _ in range(Q)]
    b = [0] * N
    for i in range(N):
        b[i] = i + 1
    for i in range(Q):
        b[a[i] - 1], b[a[i]] = b[a[i]], b[a[i] - 1]
    print(*b)
