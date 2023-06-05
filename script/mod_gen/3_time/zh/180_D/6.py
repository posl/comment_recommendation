def main():
    #读取数据
    x,y,a,b = map(int,input().split())
    #逻辑处理
    exp = 0
    while x*a <= x+b and x*a < y:
        exp += 1
        x *= a
    exp += (y-x-1)//b
    #输出结果
    print(exp)
    return 0

if __name__ == '__main__':
    main()