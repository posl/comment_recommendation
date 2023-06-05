def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if m == 0:
        print(1)
        exit()
    if n == m:
        print(0)
        exit()
    if n == 1:
        print(0)
        exit()
    if a[0] != 1:
        a.insert(0,0)
    if a[-1] != n:
        a.append(n+1)
    ans = 0
    for i in range(len(a)-1):
        if a[i+1] - a[i] - 1 > 0:
            ans += (a[i+1] - a[i] - 2) // 2 + 1
    print(ans)
