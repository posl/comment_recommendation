Synthesizing 10/10 solutions

=======
Suggestion 1

def solution():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 2

def main():
    N = int(input())
    x = 0
    while N > 0:
        x += 1
        N -= x
    print(x)

=======
Suggestion 3

def main():
    # input
    n = int(input())
    # compute
    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum >= n:
            break
    # output
    print(i)

=======
Suggestion 4

def main():
    N = int(input())
    i = 1
    sum = 0
    while True:
        sum += i
        if sum >= N:
            break
        i += 1
    print(i)

=======
Suggestion 5

def main():
    N = int(input())
    x = 1
    while True:
        if x * (x + 1) / 2 >= N:
            print(x)
            break
        else:
            x += 1

=======
Suggestion 6

def main():
    n = int(input())
    sum = 0
    for i in range(1, 10000000):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 7

def main():
    n = int(input())
    x = 0
    while x * (x + 1) / 2 < n:
        x += 1
    print(x)

=======
Suggestion 8

def main():
    #读取输入
    n = int(input())
    #计算结果
    x = int((2*n)**(1/2))
    #输出结果
    print(x)

=======
Suggestion 9

def main():
    n = int(input())
    x = 1
    while x*(x+1)//2 < n:
        x += 1
    print(x)

=======
Suggestion 10

def sum_of_natural_numbers(n):
    return int(n*(n+1)/2)
