Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 输入数据
    a, b, c = map(int, input().split())
    # 判断是否bust
    if a + b + c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 3

def main():
    a = input()
    b = a.split()
    c = int(b[0]) + int(b[1]) + int(b[2])
    if c >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 4

def main():
    a = input()
    a = a.split()
    sum = 0
    for i in range(3):
        sum += int(a[i])
    if sum >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if a+b+c >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 6

def main():
    A_1,A_2,A_3 = map(int,input().split())
    if A_1 + A_2 + A_3 >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if a + b + c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 8

def main():
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')
