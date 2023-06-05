def main():
    n,c = map(int,input().split())
    l = []
    for _ in range(n):
        a,b,c = map(int,input().split())
        l.append((a-1,c))
        l.append((b,-c))
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
main()
