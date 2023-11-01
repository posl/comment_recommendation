Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a == 0:
        print("Silver")
    elif b == 0:
        print("Gold")
    else:
        print("Alloy")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print('Gold')
    elif a == 0 and b > 0:
        print('Silver')

=======
Suggestion 3

def problem212_a():
    a,b = map(int, input().split())
    if a != 0 and b == 0:
        print("Gold")
    elif a == 0 and b != 0:
        print("

=======
Suggestion 4

def func(a, b):
    if a > 0 and b == 0:
        return "Gold"
    elif a == 0 and b > 0:
        return "Silver"
    else:
        return "Alloy"

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if a == 0 and b != 0:
        print('Silver')
    elif a != 0 and b == 0:
        print('Gold')

=======
Suggestion 6

def main():
    A,B = map(int, input().split())
    if A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")

=======
Suggestion 7

def judge(a,b):
    if a != 0 and b == 0:
        print("Gold")
    elif a == 0 and b != 0:
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 8

def main():
    A,B = map(int,input().split())
    if A>0 and B==0:
        print("Gold")
    elif A==0 and B>0:
        print("Silver")
    elif A

=======
Suggestion 9

def get_input():
    input_str = input('请输入两个整数，用空格分隔:')
    input_str = input_str.split(' ')
    input_num = []
    for i in input_str:
        input

=======
Suggestion 10

def main():
    A,B = map(int,input().split())
    if A == 0 and B > 0:
        print("Silver")
    elif A > 0 and B == 0:
        print("Gold")
