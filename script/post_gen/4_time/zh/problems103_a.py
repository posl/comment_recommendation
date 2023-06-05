Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 从标准输入读取
    a1, a2, a3 = map(int, input().split())
    # 计算并打印答案
    print(min(abs(a1 - a2) + abs(a2 - a3), abs(a1 - a3) + abs(a3 - a2), abs(a2 - a1) + abs(a1 - a3)))

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    print(max(a)-min(a))

=======
Suggestion 3

def solve(a_1, a_2, a_3):
    return max(a_1, a_2, a_3) - min(a_1, a_2, a_3)

=======
Suggestion 4

def main():
    a1,a2,a3 = map(int, input().split())
    print(abs(a1-a2)+abs(a2-a3)+abs(a3-a1)-max(abs(a1-a2),abs(a2-a3),abs(a3-a1)))

=======
Suggestion 5

def solve(a):
    a.sort()
    return a[2]-a[0]

=======
Suggestion 6

def main():
    a1, a2, a3 = map(int, input().split())
    print(min(abs(a1-a2)+abs(a2-a3), abs(a1-a3)+abs(a3-a2), abs(a2-a1)+abs(a1-a3)))

=======
Suggestion 7

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 8

def main():
    # 读取输入
    a1, a2, a3 = map(int, input().split())

    # 三种情况，a1, a2, a3 作为最小值
    # a1 作为最小值
    min_cost = abs(a2 - a1) + abs(a3 - a1)
    # a2 作为最小值
    min_cost = min(min_cost, abs(a1 - a2) + abs(a3 - a2))
    # a3 作为最小值
    min_cost = min(min_cost, abs(a1 - a3) + abs(a2 - a3))

    # 打印结果
    print(min_cost)

=======
Suggestion 9

def solve():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])
solve()
