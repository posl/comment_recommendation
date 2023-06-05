def main():
    #读入数据
    n = int(input())
    h = list(map(int, input().split()))
    #定义一个变量来记录浇水的次数
    count = 0
    #对于每个花，都要浇水，所以从0到n遍历
    for i in range(n):
        #如果当前花的高度小于它的编号，则需要浇水
        if h[i] < i + 1:
            #浇水的量就是编号减去当前花的高度
            count += i + 1 - h[i]
            #浇水后，当前花的高度就是编号
            h[i] = i + 1
    #输出浇水的次数
    print(count)
