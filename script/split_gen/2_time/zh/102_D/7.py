def solve(n, a):
    # write your code here
    # return the correct answer
    # 1. 二分法，找到最大值和最小值的中间值，然后从数组中找到最接近这个中间值的两个数，计算差值，然后比较差值和中间值的大小，如果差值小于中间值，那么中间值就是最大和最小值的绝对差值
    # 2. 从数组中找到最大值和最小值，然后从数组中找到最接近这个最大值和最小值的两个数，计算差值，然后比较差值和最大值和最小值的大小，如果差值小于最大值和最小值，那么最大值和最小值就是最大和最小值的绝对差值
    a.sort()
    min = a[0]
    max = a[n-1]
    mid = int((min + max) / 2)
    min_diff = max - min
    for i in range(n):
        if a[i] < mid:
            diff = mid - a[i]
            if min_diff > diff:
                min_diff = diff
        else:
            diff = a[i] - mid
            if min_diff > diff:
                min_diff = diff
    return min_diff
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
