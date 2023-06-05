def main():
    N, Q = map(int, input().split())
    x = [int(input()) for i in range(Q)]
    a = [i+1 for i in range(N)]
    for i in range(Q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    print(*a)
