def main():
    n, m = map(int, input().split())
    l, r = [], []
    for _ in range(m):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    print(min(r) - max(l) + 1 if min(r) - max(l) + 1 > 0 else 0)
