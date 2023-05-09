def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    b = [0] * (n + 1)
    for i in range(n):
        b[i] += a[i]
        b[i + 1] -= a[i]
    for i in range(n):
        b[i + 1] += b[i]
    for i in range(q):
        print(x[i] * n + b[n] - b[0])
