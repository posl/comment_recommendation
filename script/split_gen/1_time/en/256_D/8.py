def main():
    n = int(input())
    l = [tuple(map(int, input().split())) for _ in range(n)]
    l.sort()
    r = []
    for a in l:
        if r and r[-1][1] >= a[1]:
            continue
        if r and r[-1][1] >= a[0]:
            r[-1] = (r[-1][0], a[1])
        else:
            r.append(a)
    for a in r:
        print(*a)
