def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    a = [i for i in range(1, N+1)]
    for i in range(Q):
        for j in range(N-1):
            if a[j] == x[i]:
                a[j], a[j+1] = a[j+1], a[j]
    print(' '.join(map(str, a)))
