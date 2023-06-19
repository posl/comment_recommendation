def main():
    # 读入数据
    x,a,d,n = map(int,input().split())
    # 判断d是否为0
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    # 判断是否为好数
    if (x-a)%d == 0:
        print(0)
        return
    # 判断是否为0
    if x == 0:
        print(1)
        return
    # 判断是否为正数
    if x > 0:
        # 判断是否为正数
        if d > 0:
            # 判断是否为奇数
            if n%2 == 0:
                if x < a:
                    print(a-x)
                else:
                    print(x-a)
            else:
                if x < a:
                    print(min(a-x,x-a+d))
                else:
                    print(min(x-a,x-a+d))
        else:
            # 判断是否为奇数
            if n%2 == 0:
                if x < a:
                    print(a-x)
                else:
                    print(x-a)
            else:
                if x < a:
                    print(min(a-x,x-a+d))
                else:
                    print(min(x-a,x-a+d))
    else:
        # 判断是否为正数
        if d > 0:
            # 判断是否为奇数
            if n%2 == 0:
                if x < a:
                    print(a-x)
                else:
                    print(x-a)
            else:
                if x < a:
                    print(min(a-x,x-a+d))
                else:
                    print(min(x-a,x-a+d))
        else:
            # 判断是否为奇数
            if n%2 == 0:
                if x < a:
                    print(a-x)
                else:
                    print(x-a)
            else:
                if x < a:
                    print(min(a-x,x-a+d))
                else:
                    print(min(x-a,x-a+d))
