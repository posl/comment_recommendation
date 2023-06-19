def main():
    #读取输入
    n = int(input())
    a = list(map(int, input().split()))
    #初始化最大绝对差
    max_diff = 0
    #遍历所有可能的组合
    for i in range(n):
        for j in range(n):
            #如果是两个不同的元素
            if i != j:
                #计算绝对差
                diff = abs(a[i] - a[j])
                #如果绝对差大于最大绝对差
                if diff > max_diff:
                    #更新最大绝对差
                    max_diff = diff
    #打印最大绝对差
    print(max_diff)
