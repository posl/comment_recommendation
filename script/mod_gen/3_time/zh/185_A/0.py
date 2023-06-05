def main():
    # 从标准输入读取
    a1, a2, a3, a4 = map(int, input().split())
    # 从小到大排序
    a = sorted((a1, a2, a3, a4))
    # 用第三大的数来除以400，得到可以举行的最大竞赛数量
    print(a[2] // 400)

if __name__ == '__main__':
    main()