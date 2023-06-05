def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int,input().split())) for _ in range(k)]
    ans = 0
    for i in range(2**k):
        s = set()
        for j in range(k):
            if ((i>>j)&1):
                s.add(cd[j][0])
            else:
                s.add(cd[j][1])
        cnt = 0
        for a,b in ab:
            if a in s and b in s:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

if __name__ == '__main__':
    main()