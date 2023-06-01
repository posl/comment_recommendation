Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def max_card_sum(a, b, c):
    return max(a+b, a+c, b+c)

print(max_card_sum(3, 4, 5))
print(max_card_sum(6, 6, 6))
print(max_card_sum(99, 99, 98))

=======
Suggestion 2

def main():
    # 读取输入
    a,b,c = map(int,input().split())
    # 判断
    if a>b and a>c:
        print(a+b)
    elif b>a and b>c:
        print(b+c)
    else:
        print(c+a)

=======
Suggestion 3

def main():
    # a,b,c = map(int,input().split())
    # print(a+b+c-max(a,b,c))
    a = list(map(int,input().split()))
    print(sum(a)-max(a))

=======
Suggestion 4

def max_two_num(a,b):
    if a > b:
        return a
    else:
        return b

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    print(a+b+c-max(a,b,c))

=======
Suggestion 6

def main():
    try:
        a, b, c = map(int, input().split())
        if a < 1 or a > 100:
            raise Exception('a is not in the range of 1 to 100')
        if b < 1 or b > 100:
            raise Exception('b is not in the range of 1 to 100')
        if c < 1 or c > 100:
            raise Exception('c is not in the range of 1 to 100')
    except Exception as e:
        print(e)
    else:
        print(max(a+b, b+c, a+c))

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    print(max(a+b, b+c, c+a))
