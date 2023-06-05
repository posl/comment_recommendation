def main():
    # 读取输入
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    # 处理查询
    for i in range(q):
        x, k = map(int, input().split())
        # 从第一个元素开始计数
        count = 0
        # 记录当前元素的下标
        index = 0
        # 从第一个元素开始遍历
        for j in range(n):
            # 如果当前元素等于x，则计数加1
            if a[j] == x:
                count += 1
                # 如果计数等于k，则打印当前元素的下标，然后跳出循环
                if count == k:
                    print(j + 1)
                    break
                # 否则，更新当前元素的下标，继续遍历
                else:
                    index = j
        # 如果遍历结束后，计数还是小于k，则打印-1
        if count < k:
            print(-1)
