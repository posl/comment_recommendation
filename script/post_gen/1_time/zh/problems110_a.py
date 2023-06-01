Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    print(10*a+b+c)

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    print(max(a+b+c,a*10+b+c,a+b*10+c,a+b+c*10))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(a * 10 + b + c, a + b * 10 + c, a + b + c * 10))

=======
Suggestion 4

def max_money(A,B,C):
    max = 0
    if A+B+C > max:
        max = A+B+C
    if A+B*C > max:
        max = A+B*C
    if A*B+C > max:
        max = A*B+C
    if A*B*C > max:
        max = A*B*C
    if (A+B)*C > max:
        max = (A+B)*C
    if A*(B+C) > max:
        max = A*(B+C)
    return max

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    result = a+b+c
    result = max(result,(a+b)*c)
    result = max(result,a*(b+c))
    result = max(result,a*b*c)
    print(result)

=======
Suggestion 7

def main(a, b, c):
    # 1. 3个数都为9的情况
    if a == 9 and b == 9 and c == 9:
        return 108
    # 2. 3个数都为1的情况
    if a == 1 and b == 1 and c == 1:
        return 12
    # 3. 2个数为9，1个数为1的情况
    if (a == 9 and b == 9 and c == 1) or (a == 9 and b == 1 and c == 9) or (a == 1 and b == 9 and c == 9):
        return 91
    # 4. 2个数为1，1个数为9的情况
    if (a == 1 and b == 1 and c == 9) or (a == 1 and b == 9 and c == 1) or (a == 9 and b == 1 and c == 1):
        return 19
    # 5. 2个数为9，1个数为2的情况
    if (a == 9 and b == 9 and c == 2) or (a == 9 and b == 2 and c == 9) or (a == 2 and b == 9 and c == 9):
        return 92
    # 6. 2个数为2，1个数为9的情况
    if (a == 2 and b == 2 and c == 9) or (a == 2 and b == 9 and c == 2) or (a == 9 and b == 2 and c == 2):
        return 29
    # 7. 2个数为9，1个数为3的情况
    if (a == 9 and b == 9 and c == 3) or (a == 9 and b == 3 and c == 9) or (a == 3 and b == 9 and c == 9):
        return 93
    # 8. 2个数为3，1个数为9的情

=======
Suggestion 8

def main():
    A,B,C = map(int, input().split())
    print(max(A+B+C, A+B*C, A*B+C, A*B*C))
