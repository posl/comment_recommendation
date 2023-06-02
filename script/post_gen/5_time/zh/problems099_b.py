Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(b-a-1)

=======
Suggestion 2

def calc(a,b):
    return b-a

=======
Suggestion 3

def snow(a,b):
    """
    a:西边的塔有a米
    b:东边的塔有b米
    """
    #雪覆盖的深度总是至少1米。
    #因此，我们可以看到，雪覆盖的深度是2米。
    #两座塔的高度分别为10米和15米。
    #8 13
    #54 65
    #1 ≦ a < b < 499500(=1+2+3+...+999)
    #a,b为整数
    #没有与假设相矛盾的输入。
    #输入的所有数值都是整数。
    #限制条件
    #1 ≦ a < b < 499500(=1+2+3+...+999)
    #输入的所有数值都是整数。
    #没有与假设相矛盾的输入。
    #输入
    #输入是由标准输入给出的，格式如下：
    #a b
    #输出
    #如果雪覆盖的深度是x米，打印x为整数。
    #输入样本 1
    #8 13
    #输出样本 1
    #2
    #样本输入2
    #54 65
    #样本输出2
    #1
    #两座塔的高度分别为10米和15米。
    if a < b < 499500:
        return b - a - 1
    else:
        return None

=======
Suggestion 4

def snowDepth(a, b):
    return b - a - 1

=======
Suggestion 5

def solution(a,b):
    #a = 8
    #b = 13
    #a = 54
    #b = 65
    sum = 0
    for i in range(1,1000):
        sum = sum + i
        if sum == b - a:
            return i - 1
        if sum > b - a:
            return i - 2

=======
Suggestion 6

def getSnow(a, b):
    if a == b:
        return 0
    else:
        return (b-a-1)/2+1

=======
Suggestion 7

def snow_cover(a, b):
    sum = 0
    for i in range(1, b):
        sum += i
        if sum >= a:
            return i

=======
Suggestion 8

def calc_snow(a, b):
    return b - a - 1

=======
Suggestion 9

def solve(a,b):
    return int((1+8*(a+b))**0.5-1)//2
