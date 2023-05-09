def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    a = [i for i in range(1, N+1)]
    for i in range(Q):
        if x[i] == N:
            a[N-1], a[0] = a[0], a[N-1]
        else:
            a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    print(" ".join(map(str, a)))
