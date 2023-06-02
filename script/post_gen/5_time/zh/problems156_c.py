Synthesizing 10/10 solutions

=======
Suggestion 1

def calc_power(x, p):
    return (x - p) ** 2

=======
Suggestion 2

def findMinSum(xList):
    xList.sort()
    minSum = 0
    for x in xList:
        minSum += (x-xList[0])**2
    return minSum

=======
Suggestion 3

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 10 ** 10
    for i in range(x[0], x[-1] + 1):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i) ** 2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def min_sum_energy(n, x_list):
    min_energy = 10000000
    for i in range(1, 101):
        energy = 0
        for x in x_list:
            energy += (x - i)**2
        if energy < min_energy:
            min_energy = energy
    return min_energy

=======
Suggestion 5

def main():
    # 读入数据
    n = int(input())
    x = list(map(int, input().split()))

    # 暴力解法
    # ans = 100000000000000000
    # for p in range(1, 101):
    #     sum = 0
    #     for i in range(n):
    #         sum += (x[i] - p) ** 2
    #     ans = min(ans, sum)
    # print(ans)

    # 优化解法
    ans = 100000000000000000
    for p in range(1, 101):
        sum = 0
        for i in range(n):
            sum += (x[i] - p) ** 2
        ans = min(ans, sum)
    print(ans)

=======
Suggestion 6

def cal(x, X):
    sum = 0
    for i in range(len(X)):
        sum += (X[i] - x) ** 2
    return sum

N = int(input())
X = list(map(int, input().split()))

min = cal(1, X)
for i in range(1, 101):
    if min > cal(i, X):
        min = cal(i, X)
print(min)

=======
Suggestion 7

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = float("inf")
    for i in range(x[0], x[-1] + 1):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i) ** 2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    X = list(map(int, input().split()))
    min = 100000000
    for i in range(1,101):
        sum = 0
        for j in range(0,N):
            sum += (X[j]-i)**2
        if sum < min:
            min = sum
    print(min)

=======
Suggestion 9

def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10000000000000
    for i in range(1, 101):
        temp = 0
        for j in range(n):
            temp += (x[j] - i) ** 2
        ans = min(ans, temp)
    print(ans)

=======
Suggestion 10

def min_sum(nums):
    #计算最小值
    min_num = min(nums)
    #计算最大值
    max_num = max(nums)
    #计算最小值和最大值之间的差值
    diff = max_num - min_num
    #初始化最小值
    min_sum = 100000000
    #遍历最小值和最大值之间的差值
    for i in range(diff):
        #计算体力值
        sum = 0
        #遍历所有的坐标值
        for j in nums:
            #计算体力值
            sum += (j - min_num - i) ** 2
        #如果体力值小于最小值，则赋值给最小值
        if sum < min_sum:
            min_sum = sum
    #返回最小值
    return min_sum
