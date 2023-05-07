def main():
    #入力
    a,b,d = map(int, input().split())
    #処理
    import math
    d = math.radians(d)
    x = a * math.cos(d) - b * math.sin(d)
    y = a * math.sin(d) + b * math.cos(d)
    #出力
    print(x,y)

if __name__ == '__main__':
    main()