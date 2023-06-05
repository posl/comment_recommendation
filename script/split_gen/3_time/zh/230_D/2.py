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
    ans = 1
    cnt = 0
    i = 0
    j = 0
    while i < n and j < n:
        if l[i] <= r[j]:
            cnt += 1
            ans = max(ans, cnt)
            i += 1
        else:
            cnt -= 1
            j += 1
    print(ans)
