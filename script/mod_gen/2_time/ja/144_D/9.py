def main():
    # 入力
    a,b,x = map(int,input().split())
    # 処理
    if x >= a**2*b/2:
        ans = math.degrees(math.atan(2*(a**2*b-x)/(a**3)))
    else:
        ans = math.degrees(math.atan(a*b**2/(2*x)))
    # 出力
    print(ans)

if __name__ == '__main__':
    main()