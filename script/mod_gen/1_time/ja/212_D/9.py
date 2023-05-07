def main():
    q = int(input())
    #操作1のボールの値を入れるリスト
    balls = []
    #操作2の加算値を入れる変数
    add_num = 0
    for i in range(q):
        query = list(map(int, input().split()))
        #操作1
        if query[0] == 1:
            balls.append(query[1] - add_num)
        #操作2
        elif query[0] == 2:
            add_num += query[1]
        #操作3
        elif query[0] == 3:
            min_num = min(balls)
            print(min_num + add_num)
            balls.remove(min_num)

if __name__ == '__main__':
    main()