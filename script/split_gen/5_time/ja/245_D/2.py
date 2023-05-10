def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0 for i in range(m + 1)]
    for i in range(m + 1):
        b[i] = c[i] - sum([a[j] * b[i - j] for j in range(i)])
    print(*b)
