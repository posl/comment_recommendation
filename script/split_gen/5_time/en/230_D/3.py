def main():
    n, d = map(int, input().split())
    l = []
    r = []
    for i in range(n):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    l.sort()
    r.sort()
    i = 0
    j = 0
    ans = 0
    while i < n:
        if l[i] < r[j]:
            ans += 1
            i += 1
        else:
            j += 1
            i += 1
    print(ans)
