def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for _ in range(m):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    l.sort()
    r.sort()
    if l[m-1] > r[0]:
        print(0)
    else:
        print(r[0] - l[m-1] + 1)
