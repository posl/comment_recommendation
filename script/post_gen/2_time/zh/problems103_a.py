Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    a = list(map(int, input().split()))
    # 初始化
    ans = 10000000000
    # 遍历所有情况
    for i in range(3):
        for j in range(3):
            for k in range(3):
                # 计算总成本
                sum = abs(a[0] - a[i]) + abs(a[1] - a[j]) + abs(a[2] - a[k])
                # 更新最小总成本
                ans = min(ans, sum)
    # 输出答案
    print(ans)

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 3

def main():
    # 读取输入
    a = list(map(int, input().split()))
    # 计算最小成本
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 4

def main():
    a = list(map(int,input().split()))
    a.sort()
    ans = a[2] - a[0]
    print(ans)

=======
Suggestion 5

def main():
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, 3):
        ans += A[i] - A[i-1]
    print(ans)

=======
Suggestion 6

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[1]-a[0] + a[2]-a[1])
    return

=======
Suggestion 7

def min_cost(a):
    a.sort()
    return a[1]-a[0]+a[2]-a[1]

a = list(map(int, input().split()))
print(min_cost(a))

=======
Suggestion 8

def main():
    a = input().split()
    a = [int(a[i]) for i in range(3)]
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 9

def main():
    # 读入
    a_1, a_2, a_3 = map(int, input().split())

    # 逻辑处理
    # 1. a_1, a_2, a_3中有两个数相等
    if a_1 == a_2 or a_1 == a_3 or a_2 == a_3:
        ans = 0
    # 2. a_1, a_2, a_3中的三个数不相等
    else:
        ans = min(abs(a_1 - a_2) + abs(a_1 - a_3), abs(a_2 - a_1) + abs(a_2 - a_3), abs(a_3 - a_1) + abs(a_3 - a_2))

    # 输出
    print(ans)
