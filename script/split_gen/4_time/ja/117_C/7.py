def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        exit()
    a = [0] * (m - 1)
    for i in range(m - 1):
        a[i] = x[i + 1] - x[i]
    a.sort()
    print(sum(a[:m - n]))
