Synthesizing 10/10 solutions

=======
Suggestion 1

def sheep_safe(s,w):
    if s > w:
        print('safe')
    else:
        print('unsafe')

=======
Suggestion 2

def main():
    s,w = map(int,input().split())
    if w >= s:
        print("不安全")
    else:
        print("安全")

=======
Suggestion 3

def print_safe_or_not(s,w):
    if s > w:
        print("安全")
    else:
        print("不安全")

=======
Suggestion 4

def main():
    s, w = map(int, input().split())
    if s > w:
        print('安全')
    else:
        print('不安全')

=======
Suggestion 5

def main():
    sheep, wolf = map(int, input().split())
    if sheep > wolf:
        print("安全")
    else:
        print("不安全")

=======
Suggestion 6

def main():
    a = input()
    b = a.split()
    c = int(b[0])
    d = int(b[1])
    if c > d:
        print("安全")
    else:
        print("不安全")

=======
Suggestion 7

def problem164_a():
    s, w = map(int, input().split())
    if s > w:
        print('安全')
    else:
        print('不安全')

=======
Suggestion 8

def main():
    # 读取输入
    s,w = map(int,input().split())
    # 判断
    if s <= w:
        print("不安全")
    else:
        print("安全")

=======
Suggestion 9

def problem164_a():
    s,w = map(int, input().split())
    if w >= s:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 10

def is_safe(s,w):
    if s > w:
        return '安全'
    else:
        return '不安全'
