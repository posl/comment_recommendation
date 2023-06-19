def main():
    #读取数据
    n = int(input())
    a = list(map(int, input().split()))
    #创建一个数组，用于记录学生的学号
    ans = [0]*n
    #遍历a数组，将a[i]放到ans[a[i]-1]的位置
    for i in range(n):
        ans[a[i]-1] = i+1
    #输出结果
    print(' '.join(map(str, ans)))
