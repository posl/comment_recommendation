def main():
    n,d = map(int,input().split())
    l = []
    r = []
    for i in range(n):
        a,b = map(int,input().split())
        l.append(a)
        r.append(b)
    l.sort()
    r.sort()
    ans = 0
    for i in range(n):
        ans += 1
        if i == n-1:
            break
        if l[i+1] - r[i] >= d:
            continue
        if l[i+1] - l[i] >= d:
            continue
        if r[i+1] - l[i] >= d:
            continue
        ans += 1
    print(ans)
main()
