def main():
    # 读取输入
    a1,a2,a3 = map(int, input().split())
    # 用一个list保存
    a = [a1, a2, a3]
    # 从小到大排序
    a.sort()
    # 从小到大排序后，a[0]一定是最小的，所以，a[1]和a[2]的差值一定是最小的
    # 所以，完成所有任务的最小成本就是a[2]-a[0]
    print(a[2]-a[0])

if __name__ == '__main__':
    main()