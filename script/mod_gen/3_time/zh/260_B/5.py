def main():
    # 读入数据
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 构造一个元组列表
    # 该元组列表的元素是 (总分, 数学分数, 英语分数, 序号)
    # 序号是为了在总分、数学分数和英语分数都相同时，按照序号的升序排列
    c = [(a[i] + b[i], a[i], b[i], i + 1) for i in range(n)]
    # 按照总分、数学分数和英语分数的顺序进行排序
    c.sort(reverse=True)
    # 按照题目要求，输出结果
    for i in range(x + y + z):
        print(c[i][3])

if __name__ == '__main__':
    main()