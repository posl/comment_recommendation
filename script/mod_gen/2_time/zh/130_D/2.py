def main():
    # 读取数据
    W,H,x,y = map(int,input().split())
    # 计算面积
    area = W*H/2
    # 判断是否在中间
    if x*2 == W and y*2 == H:
        print(area,1)
    else:
        print(area,0)

if __name__ == '__main__':
    main()