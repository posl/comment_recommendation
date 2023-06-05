Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #读取数据
    n = int(input())
    #处理数据
    x = 0
    while True:
        x += 1
        if (x*(x+1)//2) >= n:
            break
    #输出数据
    print(x)
    return

=======
Suggestion 2

def problem206_b(n):
    i = 1
    while True:
        if n <= i*(i+1)/2:
            break
        else:
            i += 1
    return i

=======
Suggestion 3

def main():
    n = int(input())
    x = 0
    for i in range(1, n + 1):
        x += i
        if x >= n:
            print(i)
            break

=======
Suggestion 4

def problem206_b():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 5

def problem206_b():
    N = int(input())
    x = 0
    sum = 0
    while sum < N:
        x += 1
        sum += x
    print(x)

problem206_b()

=======
Suggestion 6

def main():
    N = int(input())
    x = 1
    while x*(x+1)/2 < N:
        x += 1
    print(x)

=======
Suggestion 7

def main():
    N = int(input())
    if (N == 1):
        print(1)
        return
    if (N == 2):
        print(2)
        return
    i = 1
    while (i * (i + 1) // 2 < N):
        i += 1
    print(i)
    return

=======
Suggestion 8

def main():
    n = int(input())
    sum = 0
    for i in range(1,n+1):
        sum += i
        if sum >= n:
            print(i)
            return

=======
Suggestion 9

def main():
    n = int(input())
    sum = 0
    i = 1
    while True:
        sum += i
        if sum >= n:
            print(i)
            break
        i += 1

=======
Suggestion 10

def calc_sum(n):
    return n*(n+1)/2
