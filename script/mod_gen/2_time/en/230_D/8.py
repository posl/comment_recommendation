def main():
    n,d = map(int,input().split())
    lrs = [list(map(int,input().split())) for _ in range(n)]
    lrs.sort()
    lrs.append([d,d])
    ans = 0
    now = 0
    for i in range(n):
        l,r = lrs[i]
        if l <= now:
            now = max(now,r)
        else:
            ans += (now-l)//d+1
            now = r
    print(ans)

if __name__ == '__main__':
    main()