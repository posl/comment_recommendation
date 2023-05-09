def main():
    n = int(input())
    lrs = [list(map(int, input().split())) for _ in range(n)]
    lrs.sort()
    l, r = lrs[0]
    for i in range(1, n):
        if r < lrs[i][0]:
            print(l, r)
            l, r = lrs[i]
        else:
            r = max(r, lrs[i][1])
    print(l, r)
