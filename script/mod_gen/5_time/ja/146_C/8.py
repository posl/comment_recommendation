def main():
    a,b,x = map(int,input().split())
    if a*10 + b*1 > x:
        print(0)
        return
    # 二分探索
    # 1以上10^9以下の整数
    ok = 10**9
    ng = 0
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if a*mid + b*len(str(mid)) <= x:
            ng = mid
        else:
            ok = mid
    print(ng)

if __name__ == '__main__':
    main()