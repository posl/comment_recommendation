def main():
    N, Q = map(int, input().split())
    a = [i for i in range(1, N + 1)]
    for i in range(Q):
        x = int(input())
        a[x - 1], a[x] = a[x], a[x - 1]
    for i in range(N):
        print(a[i], end=" ")
    print()
