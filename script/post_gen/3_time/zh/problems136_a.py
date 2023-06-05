Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B,C = map(int,input().split())
    print(C - (A - B) if (A - B) < C else 0)
main()

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if b+c <= a:
        print(0)
    else:
        print(b+c-a)

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    print(c-(a-b) if c-(a-b)>0 else 0)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a >= b + c:
        print(0)
    else:
        print(c - (a-b))

=======
Suggestion 5

def water_transfer(A,B,C):
    # A: 1号瓶最多可以装A毫升的水
    # B: 1号瓶中有B毫升的水
    # C: 2号瓶中有C毫升的水
    # 2号瓶中最多可以装A-B毫升的水
    # 每次转移水的量为B
    # 转移次数为C//B
    # 2号瓶中的水量为C-C//B*B
    return C-C//B*B

=======
Suggestion 6

def main():
    # 读取数据
    a, b, c = map(int, input().split())
    # 计算答案
    print(c - (a - b) if c - (a - b) >= 0 else c)

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    print(max(0,c-(a-b)))

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    if a > b+c:
        print(0)
    else:
        print(c-(a-b))

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if b >= a:
        print(c)
    else:
        print(c-(a-b))

=======
Suggestion 10

def main():
    A, B, C = map(int, input().split())
    print(max(0, C - (A - B)))
