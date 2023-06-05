def minTime(N, X, AB):
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]
    AB = [(A[i], B[i]) for i in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    print(AB)
    # 二分查找
    left = 0
    right = 10 ** 18
    while left < right:
        mid = (left + right) // 2
        # print(left, mid, right)
        # 计算mid时间内可以通关的关卡数
        count = 0
        for i in range(N):
            # print(i, count, mid, AB[i][0] + AB[i][1])
            if mid >= AB[i][0] + AB[i][1]:
                count += 1
            else:
                break
        # print(count)
        if count >= X:
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    minTime()