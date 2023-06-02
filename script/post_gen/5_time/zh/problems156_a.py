Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n,r = map(int, raw_input().split())
    if n >= 10:
        print r
    else:
        print r + 100 * (10 - n)

=======
Suggestion 2

def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

=======
Suggestion 3

def main():
    n, r = map(int, input().split())
    if n < 10:
        print(r + 100 * (10 - n))
    else:
        print(r)

=======
Suggestion 4

def inner_grade(n, r):
    if n >= 10:
        return r
    else:
        return r + (10 - n) * 100

=======
Suggestion 5

def inner_grade(n,r):
    inner = 0
    if n >= 10:
        inner = r
    else:
        inner = r + (10 - n) * 100
    return inner

=======
Suggestion 6

def getInnerEva(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

=======
Suggestion 7

def main():
    N, R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + (100 * (10 - N)))

=======
Suggestion 8

def main():
    # 读取输入
    input = raw_input()
    input = input.split()
    input = [int(i) for i in input]
    n = input[0]
    r = input[1]
    # 计算
    if n >= 10:
        print r
    else:
        print r + 100 * (10 - n)

=======
Suggestion 9

def getInnerGrade(n, r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)
