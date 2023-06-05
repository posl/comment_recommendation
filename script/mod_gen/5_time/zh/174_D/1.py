def main():
    #读入数据
    n = int(input())
    c = input()
    #统计白色石头的数量
    w = c.count('W')
    #统计白色石头的数量
    r = c.count('R')
    #如果白色石头的数量大于0，则可以进行操作
    if w > 0:
        #从左边开始，统计白色石头的数量
        w_left = c[:w].count('W')
        #从右边开始，统计红色石头的数量
        r_right = c[w:].count('R')
        #打印结果
        print(min(w_left, r_right))
    else:
        #如果白色石头的数量为0，则不需要操作
        print(0)

if __name__ == '__main__':
    main()