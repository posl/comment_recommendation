Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    n = int(input())

    # 处理数据
    price = int(1.08 * n)

    # 输出结果
    if price < 206:
        print('Yay!')
    elif price == 206:
        print('so-so')
    else:
        print(':(')

=======
Suggestion 2

def main():
    N = int(input())
    if N < 206:
        print("Yay!")
    elif N == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 3

def main():
    #input
    N = int(input())
    #calculation
    #output
    if N * 1.08 < 206:
        print("Yay!")
    elif N * 1.08 > 206:
        print(":(")
    else:
        print("so-so")

=======
Suggestion 4

def printAnswer(N):
    price = int(N * 1.08)
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 5

def main():
    import sys
    import math

    N = int(input())
    if N < 1 or N > 300:
        sys.exit()
    else:
        result = math.floor(1.08 * N)
        if result < 206:
            print("Yay!")
        elif result == 206:
            print("so-so")
        else:
            print(":(")

=======
Suggestion 6

def main():
    # input
    N = int(input())
    # process
    price = int(1.08 * N)
    # output
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 7

def main():
    n = int(input())
    price = int(1.08 * n)
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")

=======
Suggestion 8

def problem206_a():
    n = int(input())
    if n * 1.08 < 206:
        print("Yay!")
    elif n * 1.08 > 206:
        print(":(")
    else:
        print("so-so")

=======
Suggestion 9

def main():
    n = int(input())
    if n * 1.08 < 206:
        print('Yay!')
    elif n * 1.08 == 206:
        print('so-so')
    else:
        print(':(')

=======
Suggestion 10

def main():
    n = int(input())
    price = int(n * 1.08)
    if price < 206:
        print("Yay!")
    elif price > 206:
        print(":(")
    else:
        print("so-so")
