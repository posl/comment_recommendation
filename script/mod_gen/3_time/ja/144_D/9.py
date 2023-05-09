def main():
    #入力
    a,b,x = map(int,input().split())
    #解答
    if x <= a**2*b/2:
        ans = math.degrees(math.atan(2*x/a**2/b))
    else:
        ans = math.degrees(math.atan(2*(a**2*b-x)/a**3))
    #出力
    print(ans)

if __name__ == '__main__':
    main()