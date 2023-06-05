def main():
    q = int(input())
    #球的总数
    n = 0
    #圆柱体中球的集合，从左到右
    balls = []
    #圆柱体中球的集合，从右到左
    balls_reverse = []
    #球的总数
    for i in range(q):
        query = input().split()
        #如果是插入
        if query[0] == '1':
            #在圆柱体的右端插入c个球，每个球上写有数字x。
            x = int(query[1])
            c = int(query[2])
            #在圆柱体的右端插入c个球，每个球上写有数字x。
            for i in range(c):
                balls.append(x)
                balls_reverse.insert(0,x)
            n += c
        #如果是取出
        elif query[0] == '2':
            #取出圆柱体中最左边的c个球，并打印出被取出的球上所写的数字之和。
            c = int(query[1])
            sum = 0
            #取出圆柱体中最左边的c个球
            for i in range(c):
                sum += balls[0]
                balls.pop(0)
                balls_reverse.pop()
            #打印出被取出的球上所写的数字之和。
            print(sum)

if __name__ == '__main__':
    main()