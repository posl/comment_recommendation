def main():
    h,w,a,b = map(int,input().split())
    print(h,w,a,b)
    print('----------------------')
    print(h*w,a+b)
    print('----------------------')
    print(h*w/(a+b))
    print('----------------------')
    print(h*w//(a+b))
    print('----------------------')
    #縦横を入れ替えた場合の数を求める
    h,w = w,h
    print(h,w,a,b)
    print('----------------------')
    print(h*w,a+b)
    print('----------------------')
    print(h*w/(a+b))
    print('----------------------')
    print(h*w//(a+b))
    print('----------------------')
    print((h*w//(a+b)) * (h*w//(a+b)))

if __name__ == '__main__':
    main()