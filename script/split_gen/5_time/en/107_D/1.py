def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i - 1] + a[i]
    m = [0] * n
    m[0] = a[0]
    for i in range(1, n):
        m[i] = max(m[i - 1], a[i])
    for i in range(n):
        m[i] = max(m[i], (b[i] + m[i - 1]) / (i + 1))
    print(m[-1])
