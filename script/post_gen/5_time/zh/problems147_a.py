Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = [int(i) for i in input().split()]
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if a+b+c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 3

def main():
    # input
    A_1, A_2, A_3 = map(int, input().split())

    # compute

    # output
    if A_1 + A_2 + A_3 >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 4

def main():
    a1,a2,a3 = map(int,input().split())
    if a1+a2+a3 >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 5

def main():
    a = input()
    a_list = a.split()
    a_list = [int(i) for i in a_list]
    if sum(a_list) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 6

def main():
    a = input()
    b = input()
    c = input()
    if a + b + c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 7

def main():
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 8

def main():
    # 读入一行输入
    line = input()
    # 用空格分隔开来
    a = line.split()
    # 把每个数字转换成int类型
    a = list(map(int, a))
    # 求和
    s = sum(a)
    # 输出
    if s >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 9

def main():
    # 解答开始
    a1,a2,a3 = map(int,input().split())
    if a1+a2+a3 >= 22:
        print("bust")
    else:
        print("win")
    # 解答结束

=======
Suggestion 10

def main():
    a = input().split()
    sum = 0
    for i in a:
        sum += int(i)
    if sum >= 22:
        print("bust")
    else:
        print("win")
