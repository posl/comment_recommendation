Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def isContain7(n):
    if n % 10 == 7:
        return True
    elif n / 10 == 0:
        return False
    else:
        return isContain7(n / 10)

=======
Suggestion 2

def main():
    n = int(input())
    if n % 10 == 7:
        print("是")
    elif n // 10 % 10 == 7:
        print("是")
    elif n // 100 % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 3

def main():
    n = int(input())
    if n % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 4

def main():
    #输入
    N = int(input())
    #处理
    #N是否包含数字7
    #算出百位，十位，个位
    #百位
    N_100 = N//100
    #十位
    N_10 = N%100//10
    #个位
    N_1 = N%10
    #输出
    if N_100 == 7 or N_10 == 7 or N_1 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 5

def is_contain_seven(n):
    if n % 10 == 7:
        return True
    elif n // 10 % 10 == 7:
        return True
    elif n // 100 % 10 == 7:
        return True
    else:
        return False

n = int(input())

=======
Suggestion 6

def is_7_in(n):
    return "是" if "7" in str(n) else "否"

=======
Suggestion 7

def isSeven(n):
    if n % 10 == 7 or (n // 10) % 10 == 7 or n // 100 == 7:
        return True
    else:
        return False

=======
Suggestion 8

def main():
    N = int(input())
    if N % 10 == 7 or N // 10 % 10 == 7 or N // 100 % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 9

def solve():
    N = int(input())
    if N % 10 == 7:
        print('是')
    else:
        print('否')
