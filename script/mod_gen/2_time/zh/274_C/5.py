def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = [0] * (2 * n + 1)
    for i in range(n):
        d[a[i]] = 1
    for i in range(2 * n, 0, -1):
        d[i // 2] += d[i]
    for i in range(1, 2 * n + 1):
        print(d[i])
main()
