def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n - m + 1)
    for i in range(n - m + 1):
        b[i] = sum(a[i:i + m])
    c = []
    for i in range(n - m + 1):
        c.append(b[i] + sum(a[i + m:]))
    print(max(c))
