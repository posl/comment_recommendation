Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n):
    x = 0
    while (x+1)*(x+2)/2 < n:
        x += 1
    return x+1

=======
Suggestion 2

def main():
    # 读取输入
    input = int(input())
    # 处理
    day = 1
    sum = 0
    while True:
        sum += day
        if sum >= input:
            break
        day += 1
    # 输出
    print(day)

=======
Suggestion 3

def getN():
    N = int(input())
    return N

=======
Suggestion 4

def solve():
    #n = int(input())
    n = 12
    sum = 0
    for i in range(1, n + 1):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 5

def main():
    n = int(input())
    sum = 0
    for i in range(1,n+1):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 6

def get_day(N):
    sum = 0
    for i in range(1, N+1):
        sum += i
        if sum >= N:
            return i

=======
Suggestion 7

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
Suggestion 8

def get_num(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
        if sum >= n:
            return i
    return 0

=======
Suggestion 9

def main():
    n = int(input())
    x = 1
    y = 0
    while y < n:
        y += x
        x += 1
    print(x - 1)

=======
Suggestion 10

def main():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        sum += i
        if sum >= N:
            print(i)
            break
