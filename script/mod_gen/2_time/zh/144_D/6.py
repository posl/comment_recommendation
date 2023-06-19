def main():
    #读取数据
    a,b,x = map(int,input().split())
    #计算
    if x >= a**2*b/2:
        #当水满的时候，计算
        h = (a**2*b-x)*2/a**2
        #计算角度
        import math
        ans = math.atan2(h,a)
        #转换为角度
        ans = ans*180/math.pi
    else:
        #当水不满的时候，计算
        h = x*2/a/b
        #计算角度
        import math
        ans = math.atan2(b,h)
        #转换为角度
        ans = ans*180/math.pi
    #打印结果
    print(ans)

if __name__ == '__main__':
    main()