Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem207_a():
    a, b, c = map(int, input().split())
    print(max(a+b, a+c, b+c))

=======
Suggestion 2

def main():
    a,b,c = map(int, input().split())
    print(a+b+c)

=======
Suggestion 3

def max_sum():
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a == b == c:
        print(a+b)
    elif a == b:
        print(a+c)
    elif a == c:
        print(a+b)
    elif b == c:
        print(b+a)
    else:
        print(max(a,b,c)*2)

=======
Suggestion 4

def max_sum(a,b,c):
    if a >= b and a >= c:
        return a + max(b,c)
    elif b >= a and b >= c:
        return b + max(a,c)
    else:
        return c + max(a,b)

=======
Suggestion 5

def main():
    num_list = input().split()
    num_list = [int(i) for i in num_list]
    num_list.sort()
    print(sum(num_list[-2:]))

=======
Suggestion 6

def max_sum():
    a, b, c = map(int, input().split())
    print(a + b + c - min(a, b, c))
    return

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    print(max(a+b,b+c,c+a))

=======
Suggestion 8

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 输出结果
    print(a + b + c - min(a, b, c))

=======
Suggestion 9

def main():
    a,b,c = map(int, input().split())
    print(max(a+b, a+c, b+c))
