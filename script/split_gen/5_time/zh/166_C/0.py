def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    is_good = [True] * n
    for i in range(m):
        if h[a[i]] <= h[b[i]]:
            is_good[a[i]] = False
        if h[b[i]] <= h[a[i]]:
            is_good[b[i]] = False
    print(is_good.count(True))
