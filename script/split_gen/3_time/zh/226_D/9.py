def main():
    #输入
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    #预处理
    x.sort()
    y.sort()
    #计算
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            #计算两点的x,y差值
            dx = x[j] - x[i]
            dy = y[j] - y[i]
            #计算两点的x,y差值的最小公约数
            #这里使用了欧几里得算法
            #https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%85%AC%E7%BA%A6%E6%95%B0%E5%92%8C%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0
            #https://baike.baidu.com/item/%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%97%E7%AE%97%E6%B3%95/570892?fr=aladdin
            #https://baike.baidu.com/item/%E8%BE%97%E8%BD%AC%E8%BD%AE%E7%AE%97%E6%B3%95/1036309?fr=aladdin
            #https://baike.baidu.com/item/%E4%BA%8C%E5%88%86%E6%B3%95/1036309?fr=aladdin
            #https://baike.baidu.com/item/%E5%85%B3%E4%BA%8E%E6%9C%80%E5%A4%A7%E5%85%AC%E7%BA%A6%E6%95%B0%E5%92%8C%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0%E7%9A%84%E5%AE%9A%E7%90%
