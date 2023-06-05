def main():
    n,c = map(int, input().split())
    l = []
    for i in range(n):
        a,b,d = map(int, input().split())
        l.append((a,d))
        l.append((b+1,-d))
    l.sort()
    ans = 0
    fee = 0
    t = 0
    for x,y in l:
        if x != t:
            ans += min(c,fee)*(x-t)
            t = x
        fee += y
    print(ans)

if __name__ == '__main__':
    main()