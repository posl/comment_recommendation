def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    # 1-indexed
    a = [i for i in range(1, N+1)]
    # 1-indexed
    b = [i for i in range(1, N+1)]
    for i in range(Q):
        b[a[x[i]]] = a[x[i]-1]
        b[a[x[i]-1]] = a[x[i]]
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    for i in range(1, N+1):
        print(b[i], end=" ")
