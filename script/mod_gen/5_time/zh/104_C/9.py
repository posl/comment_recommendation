def main():
    #输入数据
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    #初始化
    ans = float('inf')
    #枚举所有解决问题的方法
    for i in range(2**D):
        #记录解决问题的总数
        num = 0
        #记录解决问题的总分
        score = 0
        #记录最后一题
        last = -1
        for j in range(D):
            #如果解决了第j题
            if (i>>j)&1:
                #记录解决问题的总数
                num += pc[j][0]
                #记录解决问题的总分
                score += pc[j][0]*(j+1)*100 + pc[j][1]
            #否则
            else:
                #记录最后一题
                last = j
        #如果解决问题的总分不够
        if score < G:
            #需要解决的最后一题
            s = 100*(last+1)
            #需要解决的问题数
            need = (G-score+s-1)//s
            #如果需要解决的问题数超过了这道题的数量
            if need >= pc[last][0]:
                continue
            #更新解决问题的总数
            num += need
        #更新解决问题的总数
        ans = min(ans, num)
    #输出结果
    print(ans)

if __name__ == '__main__':
    main()