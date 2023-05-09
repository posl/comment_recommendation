def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m + 1)
    for i in range(m + 1):
        b[i] = c[i]
        for j in range(n + 1):
            if i >= j:
                b[i] -= a[j] * b[i - j]
    print(*b)
