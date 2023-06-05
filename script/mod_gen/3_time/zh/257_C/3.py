def func(n, s, w):
    # 1. 二分查找
    # 2. 计算每一个X对应的f(x)
    # 3. 找到最大的f(x)
    # 4. 找到最大的f(x)对应的X
    # 5. 打印最大的f(x)
    start = 1
    end = max(w)
    while start <= end:
        mid = (start + end) // 2
        # print("start = {}, end = {}, mid = {}".format(start, end, mid))
        if f(mid, n, s, w):
            start = mid + 1
        else:
            end = mid - 1
    print(start - 1)

if __name__ == '__main__':
    func()