Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 2

def get_min_cost(a1,a2,a3):
    cost = 1000000
    if a1 > a2:
        cost = a1 - a2
    else:
        cost = a2 - a1
    if a1 > a3:
        cost = cost + a1 - a3
    else:
        cost = cost + a3 - a1
    return cost

=======
Suggestion 3

def main():
    a_1, a_2, a_3 = map(int, input().split())
    print(min(abs(a_1-a_2)+abs(a_2-a_3), abs(a_1-a_3)+abs(a_3-a_2), abs(a_2-a_1)+abs(a_1-a_3)))

=======
Suggestion 4

def minimum_cost(a):
    return min(abs(a[1]-a[0])+abs(a[2]-a[1]),abs(a[2]-a[0])+abs(a[1]-a[2]),abs(a[0]-a[1])+abs(a[2]-a[0]))

=======
Suggestion 5

def main():
    a = input().split()
    a = list(map(int, a))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 6

def abs(a,b):
  if a>b:
    return a-b
  else:
    return b-a

=======
Suggestion 7

def solve():
    #这里写你的代码
    a = list(map(int, input().split()))
    a.sort()
    print(a[2]-a[0])

=======
Suggestion 8

def main():
    # 读取输入
    a = list(map(int, input().split()))

    # 从小到大排序
    a.sort()

    # 计算最小总成本
    ans = a[2] - a[0]

    # 输出答案
    print(ans)
