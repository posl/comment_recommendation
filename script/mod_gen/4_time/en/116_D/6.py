def main():
    N,K = map(int,input().split())
    sushis = []
    for i in range(N):
        t,d = map(int,input().split())
        sushis.append((d,t))
    sushis.sort(reverse=True)
    kinds = set()
    kinds.add(sushis[0][1])
    base = sushis[0][0]
    bonus = 1
    ans = base + bonus**2
    for i in range(1,N):
        if len(kinds) == K:
            if sushis[i][1] in kinds:
                base += sushis[i][0]
                if base + bonus**2 > ans:
                    ans = base + bonus**2
            else:
                break
        else:
            base += sushis[i][0]
            kinds.add(sushis[i][1])
            bonus += 1
            if base + bonus**2 > ans:
                ans = base + bonus**2
    print(ans)

if __name__ == '__main__':
    main()