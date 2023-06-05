Synthesizing 10/10 solutions (Duplicates hidden)

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
    A = input().split()
    A = [int(a) for a in A]
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 3

def main():
    A = list(map(int, input().split()))
    if sum(A) >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 5

def main():
    # 读取输入
    a1, a2, a3 = map(int, input().split())
    # 判断是否bust
    if a1 + a2 + a3 >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 6

def main():
    A = list(map(int, input().split()))
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 7

def main():
    line = input()
    a = line.split(" ")
    sum = 0
    for i in range(3):
        sum += int(a[i])
    if sum >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 8

def main():
    a = input()
    b = input()
    c = input()
    if a + b + c >= 22:
        print('bust')
    else:
        print('win')
