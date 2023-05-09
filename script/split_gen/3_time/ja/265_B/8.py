def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(m)]
    cur = t
    for i in range(n-1):
        cur -= a[i]
        if cur <= 0:
            print('No')
            exit()
        cur = min(cur + xy[i][1], t)
    print('Yes')
