def main():
    n,d = map(int, input().split())
    l = []
    r = []
    for i in range(n):
        a,b = map(int, input().split())
        l.append(a)
        r.append(b)
    l.sort()
    r.sort()
    ans = 0
    i = 0
    j = 0
    while i < n:
        if l[i] > r[j]:
            j += 1
        else:
            i += 1
            j += 1
            ans += 1
    print(ans)
