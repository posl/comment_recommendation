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
    ans = 0
    i = 0
    j = 0
    count = 0
    while i < n:
        if l[i] <= r[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        ans = max(ans, count)
    print(ans)
