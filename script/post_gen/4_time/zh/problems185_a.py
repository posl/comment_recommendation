Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    print(min(a))

=======
Suggestion 2

def main():
    #输入
    a = list(map(int, input().split()))
    #处理
    a.sort()
    #输出
    if a[0] + a[1] + a[2] >= a[3]:
        print(3)
    elif a[0] + a[1] >= a[2] + a[3]:
        print(2)
    elif a[0] + a[1] >= a[3]:
        print(2)
    else:
        print(1)

=======
Suggestion 3

def main():
    a = [int(i) for i in input().split()]
    a.sort()
    print(a[0])

=======
Suggestion 4

def solve():
    a = [int(i) for i in input().split(" ")]
    a.sort()
    print(a[0])

solve()

=======
Suggestion 5

def main():
    a = map(int, raw_input().split())
    print min(a) / 100

=======
Suggestion 6

def main():
    # 读入数据
    a1, a2, a3, a4 = map(int, input().split())
    # 计算可以举行的最大比赛数量
    print(min(a1, a2, a3, a4))

=======
Suggestion 7

def solve():
    s = input()
    a = s.split()
    for i in range(len(a)):
        a[i] = int(a[i])
    if a.count(100) == 1 and a.count(200) == 1 and a.count(300) == 1 and a.count(400) == 1:
        print(1)
    else:
        print(0)

=======
Suggestion 8

def solve():
    #读取输入
    a1,a2,a3,a4 = map(int,input().split())

    #处理
    if a1+a2+a3+a4 <= 100:
        print(4)
    elif a1+a2+a3 <= 100:
        print(3)
    elif a1+a2 <= 100:
        print(2)
    elif a1 <= 100:
        print(1)
    else:
        print(0)

=======
Suggestion 9

def main():
    a = input().split()
    a = [int(i) for i in a]
    a.sort()
    print(a[0])

=======
Suggestion 10

def solve():
    a1, a2, a3, a4 = map(int, input().split())
    res = 0
    if a1 == 100:
        res += 1
    if a2 == 100:
        res += 1
    if a3 == 100:
        res += 1
    if a4 == 100:
        res += 1
    print(res)
