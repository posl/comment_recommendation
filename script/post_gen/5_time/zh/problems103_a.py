Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 2

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2]-A[0])

=======
Suggestion 3

def min_cost(a1, a2, a3):
    min_cost = 100000000
    # 1 2 3
    cost = abs(a1-a2) + abs(a2-a3) + abs(a3-a1)
    if cost < min_cost:
        min_cost = cost
    # 1 3 2
    cost = abs(a1-a3) + abs(a3-a2) + abs(a2-a1)
    if cost < min_cost:
        min_cost = cost
    # 2 1 3
    cost = abs(a2-a1) + abs(a1-a3) + abs(a3-a2)
    if cost < min_cost:
        min_cost = cost
    # 2 3 1
    cost = abs(a2-a3) + abs(a3-a1) + abs(a1-a2)
    if cost < min_cost:
        min_cost = cost
    # 3 1 2
    cost = abs(a3-a1) + abs(a1-a2) + abs(a2-a3)
    if cost < min_cost:
        min_cost = cost
    # 3 2 1
    cost = abs(a3-a2) + abs(a2-a1) + abs(a1-a3)
    if cost < min_cost:
        min_cost = cost
    return min_cost

=======
Suggestion 4

def main():
    # 读入数据
    a = list(map(int, input().split()))

    # 初始化
    cost = 0
    # 从小到大排序
    a.sort()

    # 求出平均值
    mean = sum(a) / len(a)

    # 求出中位数
    median = a[1]

    # 求出最小值
    minimum = a[0]

    # 求出最大值
    maximum = a[2]

    # 求出最小总成本
    cost = maximum - minimum

    # 输出结果
    print(cost)

=======
Suggestion 5

def min_cost(a, b, c):
    return min(abs(a-b)+abs(b-c), abs(a-c)+abs(c-b), abs(b-a)+abs(a-c), abs(b-c)+abs(c-a), abs(c-a)+abs(a-b), abs(c-b)+abs(b-a))

a, b, c = map(int, input().split())
print(min_cost(a, b, c))

=======
Suggestion 6

def solve():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])
