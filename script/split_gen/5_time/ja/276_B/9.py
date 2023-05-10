def main():
    n, m = map(int, input().split())
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    for i in range(1, m + 1):
        a[i], b[i] = map(int, input().split())
    c = [0] * (n + 1)
    for i in range(1, m + 1):
        c[a[i]] += 1
        c[b[i]] += 1
    for i in range(1, n + 1):
        print(c[i])
