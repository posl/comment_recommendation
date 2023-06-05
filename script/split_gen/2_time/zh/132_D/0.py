def main():
    # 读入数据
    n = int(input())
    d = list(map(int, input().split()))
    # 排序
    d.sort()
    # 找到中位数
    if n%2 == 0:
        k = (d[int(n/2)-1] + d[int(n/2)])/2
    else:
        k = d[int((n-1)/2)]
    # 找到中位数后面第一个不等于中位数的数字
    i = 0
    while d[int(n/2)+i] == k:
        i += 1
    # 计算答案
    print(i)
