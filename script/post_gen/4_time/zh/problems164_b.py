Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int,input().split())
    while a > 0 and c > 0:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
        if a <= 0:
            print("No")
            break

=======
Suggestion 2

def main():
    a, b, c, d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
        if a <= 0:
            print("No")
            break

=======
Suggestion 3

def get_input():
    a, b, c, d = map(int, input().split())
    return a, b, c, d

=======
Suggestion 4

def judge_win(a,b,c,d):
    while True:
        c -= b
        if c <= 0:
            return True
        a -= d
        if a <= 0:
            return False

=======
Suggestion 5

def main():
    # 读取输入
    line = input()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    d = int(line[3])

    # 模拟战斗
    while True:
        c = c - b
        if c <= 0:
            print("Yes")
            break
        a = a - d
        if a <= 0:
            print("No")
            break

=======
Suggestion 6

def main():
    a,b,c,d = map(int, input().split())
    while a > 0 and c > 0:
        c -= b
        a -= d
    if c <= 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    a,b,c,d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print('Yes')
            break
        a -= d
        if a <= 0:
            print('No')
            break

=======
Suggestion 8

def main():
    a,b,c,d = map(int, input().split())
    while a>0 and c>0:
        c -= b
        if c<=0:
            print('Yes')
            break
        a -= d
        if a<=0:
            print('No')
            break
