Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a1, a2, a3 = map(int, input().split())
    if a1 + a2 + a3 >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 2

def main():
    A = input()
    A = A.split()
    A = [int(n) for n in A]
    if sum(A) >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 3

def main():
    # 读取输入
    a = [int(x) for x in input().split()]
    # 计算
    total = sum(a)
    # 输出
    if total >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 4

def main():
    # input
    A_1, A_2, A_3 = map(int, input().split())
    # check
    if A_1 + A_2 + A_3 >= 22:
        # output
        print('bust')
    else:
        # output
        print('win')

=======
Suggestion 5

def main():
    a1, a2, a3 = map(int, input().split())
    if a1 + a2 + a3 >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 6

def problem147_a():
    a = input()
    a = a.split()
    sum = 0
    for i in a:
        sum += int(i)
    if sum >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 7

def main():
    A_1, A_2, A_3 = map(int, input().split())
    if A_1 + A_2 + A_3 >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 8

def main():
    a = input()
    a = a.split(' ')
    a = list(map(int, a))
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 9

def main():
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 10

def main():
    # input
    A_1, A_2, A_3 = map(int, input().split())

    # compute

    # output
    if A_1 + A_2 + A_3 >= 22:
        print("bust")
    else:
        print("win")
