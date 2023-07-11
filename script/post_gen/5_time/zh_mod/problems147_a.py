Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    input_line = input()
    # 用空格分割输入
    input_list = input_line.split()
    # 将输入转换为整数
    input_int_list = [int

=======
Suggestion 2

def main():
    a1, a2, a3 = map(int, input().split())
    if a1 + a2 + a3 >= 22:
        print("bust")

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 4

def main():
    A = list(map(int, input().split()))
    if (A[0] + A[1] + A[2]) >= 22:
        print("bust")

=======
Suggestion 5

def judge_bust(a1, a2, a3):
    if a1 + a2 + a3 >= 22:
        return 'bust'
    else:
        return 'win'

=======
Suggestion 6

def main():
    a1,a2,a3 = map(int,input().split())
    if a1+a2+a3 >= 22:
        print("bust")
    else:

=======
Suggestion 7

def main():
    a1, a2, a3 = map(int, input().split())
    if a1 + a2 + a3 >= 22:
        print('bust')

=======
Suggestion 8

def main():
    a = input().split()
    a = [int(i) for i in a]
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')
