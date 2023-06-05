def main():
    #读取输入
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    #如果k>n+1的话，那么必须选n+1个数，这时候只有一种可能，就是所有的数都选上
    if k > n + 1:
        k = n + 1
    #计算最小和
    min_sum = 0
    for i in range(k):
        min_sum += 10 ** 100 + i
    #计算最大和
    max_sum = 0
    for i in range(n, n - k, -1):
        max_sum += 10 ** 100 + i
    #计算和的可能种类数
    count = max_sum - min_sum + 1
    #输出结果
    print(count % mod)
