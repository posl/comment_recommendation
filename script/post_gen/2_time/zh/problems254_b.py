Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print(n%100)

=======
Suggestion 2

def main():
    # 读入N
    N = int(input())

    # 请在此处写下您的代码
    # 请使用print()输出答案
    print(N%100)

=======
Suggestion 3

def last_two_digits(n):
    if n < 100 or n > 999:
        return None
    return n % 100

=======
Suggestion 4

def main():
    N = int(input())
    print(str(N)[-2:])

=======
Suggestion 5

def last_two_digits(N):
    if N < 100 or N > 999:
        print("N is not in the range of 100 to 999.")
    else:
        print(N%100)

N = int(input())
last_two_digits(N)

=======
Suggestion 6

def main():
    n = int(input())
    print("{:02d}".format(n % 100))

=======
Suggestion 7

def main():
    num = int(input())
    print(str(num)[-2:])

=======
Suggestion 8

def last_two_digits():
    n = int(input())
    print(n%100)

=======
Suggestion 9

def main():
    number = input()
    print(number[-2:])
