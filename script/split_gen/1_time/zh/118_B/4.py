def main():
    # 读取输入
    n,m = map(int,input().split())
    a = [[int(i) for i in input().split()] for j in range(n)]
    # print(a)
    # 初始化
    like = [0 for i in range(m)]
    # print(like)
    # 统计喜欢的次数
    for i in range(n):
        for j in range(a[i][0]):
            like[a[i][j+1]-1] += 1
    # print(like)
    # 统计喜欢的食物数
    count = like.count(n)
    # print(count)
    # 输出
    print(count)
