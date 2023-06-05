def main():
    #输入
    x,y,r = map(float, input().split())
    #计算
    x1 = int(x-r)
    x2 = int(x+r)
    count = 0
    for i in range(x1,x2+1):
        #y = sqrt(r^2-(x-x0)^2)+y0
        y1 = y + (r**2-(i-x)**2)**0.5
        y2 = y - (r**2-(i-x)**2)**0.5
        count += int(y1) - int(y2)
    #输出
    print(count*4+4)
main()
