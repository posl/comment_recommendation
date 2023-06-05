def main():
    print("问题219：午餐盒")
    print("输入午餐盒数目：")
    n = int(input())
    print("输入章鱼烧和鱼形蛋糕的个数：")
    x, y = map(int, input().split())
    print("输入午餐盒的信息：")
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print("最少午餐盒数目为：")
    print(solve(n, x, y, a, b))

if __name__ == '__main__':
    main()