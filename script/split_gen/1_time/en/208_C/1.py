def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append((i, a[i]))
    b.sort(key=lambda x: x[1])
    c = [k // n] * n
    k %= n
    for i in range(k):
        c[b[i][0]] += 1
    for i in range(n):
        print(c[i])
