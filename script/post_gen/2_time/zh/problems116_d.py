Synthesizing 10/10 solutions

=======
Suggestion 1

def get_min_watering_times(n, h):
    min_watering_times = 0
    for i in range(n):
        if i == 0:
            if h[i] > 0:
                min_watering_times += h[i]
        else:
            if h[i] > h[i - 1]:
                min_watering_times += h[i] - h[i - 1]
    return min_watering_times

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)
    ans = 0
    for i in range(1, n + 1):
        if h[i - 1] < h[i]:
            ans += h[i] - h[i - 1]
        if h[i + 1] < h[i]:
            ans += h[i] - h[i + 1]
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while sum(h) > 0:
        l = 0
        r = 0
        for i in range(N):
            if h[i] > 0:
                l = i
                break
        for i in range(l, N):
            if h[i] == 0:
                r = i - 1
                break
            elif i == N - 1:
                r = N - 1
                break
        for i in range(l, r + 1):
            h[i] -= 1
        ans += 1
    print(ans)

=======
Suggestion 4

def get_min_watering_times():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)
    count = 0
    for i in range(1, N+1):
        if h[i-1] < h[i] and h[i] > h[i+1]:
            count += 1
    return count

=======
Suggestion 5

def water_flowers(N, h):
    # 从左到右遍历花坛
    # 如果左边比右边高，就浇水，浇水量为左边高度减去右边高度
    # 如果右边比左边高，就不浇水，浇水量为0
    # 如果左右相等，就不浇水，浇水量为0
    # 浇水量累加，就是最小浇水次数
    # 浇水过程中，花坛的高度也会变化
    # 浇水过程中，花坛的高度不能为负数
    # 浇水过程中，花坛的高度不能超过100
    # 浇水过程中，花坛的高度不能超过左右两边的最小值
    # 浇水过程中，花坛的高度不能超过左右两边的最大值
    # 浇水过程中，花坛的高度不能超过左右两边的平均值
    # 浇水过程中，花坛的高度不能超过左右两边的中位数
    # 浇水过程中，花坛的高度不能超过左右两边的众数
    # 浇水过程中，花坛的高度不能超过左右两边的最大值和最小值的差值
    # 浇水过程中，花坛的高度不能超过左右两边的最大值和最小值的差值的平方
    # 浇水过程中，花坛的高度不能超过左右两边的最大值和最小值的差值的立方
    # 浇水过程中，花坛的高度不能超过左右两边的最大值和最小值的差值的立方根
    # 浇水过程

=======
Suggestion 6

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += h[i]
        else:
            if h[i] > h[i - 1]:
                ans += h[i] - h[i - 1]
    print(ans)

=======
Suggestion 7

def waterFlower(N, h):
    result = 0
    if N == 1:
        return h[0]
    for i in range(N-1):
        if h[i] < h[i+1]:
            result += h[i+1] - h[i]
    result += h[0]
    return result

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0,0)
    h.append(0)
    result = 0
    for i in range(1,N+1):
        if h[i] > h[i-1] and h[i] > h[i+1]:
            result += 1
    print(result)

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)

    ans = 0
    for i in range(1, n+1):
        if h[i-1] < h[i] > h[i+1]:
            ans += 1
        if h[i-1] > h[i] < h[i+1]:
            ans += 1

    print(ans)
