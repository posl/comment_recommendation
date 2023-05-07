def main():
    n, m = map(int, input().split())
    l = 0
    r = n + 1
    for i in range(m):
        li, ri = map(int, input().split())
        l = max(l, li)
        r = min(r, ri)
    print(max(r - l + 1, 0))
