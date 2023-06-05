def main():
    # 读入数据
    a,b = map(int,input().split())
    # 二分查找
    # 1. 求解函数
    def f(x):
        return x + a/((x+1)**0.5)
    # 2. 二分查找
    left = 0
    right = 10**18
    while right - left > 10**(-6):
        mid = (left + right) / 2
        if f(mid) < f(mid + b):
            right = mid
        else:
            left = mid
    # 3. 输出结果
    print(f(left))

if __name__ == '__main__':
    main()