Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a1,a2,a3 = map(int,input().split())
    if a1+a2+a3 >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 2

def main():
    a = input().split()
    a = [int(i) for i in a]
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 3

def main():
    A1,A2,A3 = map(int,input().split())
    if A1+A2+A3 >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if a+b+c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 5

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 判断
    if a + b + c >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    if a+b+c >= 22:
        print('bust')
    else:
        print('win')

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
    a = input().split()
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
    if sum >= 22:
