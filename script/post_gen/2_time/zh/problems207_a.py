Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(a+b+c-max(a, b, c))

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(max(a+b, b+c, c+a))

=======
Suggestion 3

def main():
    # 读入
    a, b, c = map(int, input().split())

    # 处理
    print(a + b + c - min(a, b, c))

=======
Suggestion 4

def get_max_sum(a, b, c):
    """
    获取两个数的最大和
    :param a:
    :param b:
    :param c:
    :return:
    """
    max_sum = 0
    if a > b and a > c:
        max_sum = a + max(b, c)
    elif b > a and b > c:
        max_sum = b + max(a, c)
    elif c > a and c > b:
        max_sum = c + max(a, b)
    else:
        max_sum = a + b
    return max_sum

=======
Suggestion 5

def get_cards():
    cards = input().split(' ')
    cards = [int(i) for i in cards]
    return cards

=======
Suggestion 6

def main():
    A,B,C = map(int, input().split())
    print(A+B+C-max(A,B,C))
main()

=======
Suggestion 7

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 计算和
    print(a + b + c - min(a, b, c))

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    print(a + b + c - min(a, b, c))

=======
Suggestion 9

def main():
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    print(a+b+c)

=======
Suggestion 10

def problem207_a():
    a,b,c=map(int,input().split())
    print(max(a+b,b+c,c+a))
problem207_a()
