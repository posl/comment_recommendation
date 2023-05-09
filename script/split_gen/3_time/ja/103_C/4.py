def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a.reverse()
    f = [0] * N
    f[0] = a[0]
    for i in range(1, N):
        f[i] = f[i - 1] + a[i]
    print(f[N - 1])
