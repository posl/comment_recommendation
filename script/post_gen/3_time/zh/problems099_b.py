Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(b-a-1)

=======
Suggestion 2

def getSnowDepth(a,b):
    """
    根据题目中的条件，可以得出如下公式：
    a = x + (x+1) + (x+2) + ... + (x+n)
    b = (x+1) + (x+2) + ... + (x+n) + (x+n+1)
    化简得：
    a = nx + n(n+1)/2
    b = (n+1)(n+2)/2 + nx
    化简得：
    b = 2a + n + 1
    n = b - 2a - 1
    """
    n = b - 2*a - 1
    return n

=======
Suggestion 3

def snow_depth(a,b):
    x = b - a
    return x * (x + 1) // 2 - a

=======
Suggestion 4

def calc(a, b):
    return b - a

=======
Suggestion 5

def snow_depth(a, b):
    # 1+2+3+...+n = n*(n+1)/2
    # a = x*(x+1)/2
    # b = y*(y+1)/2
    # b-a = y*(y+1)/2 - x*(x+1)/2
    #     = (y-x)*(y+x+1)/2
    #     = 499500
    # y-x = 499500*2/(y+x+1)
    # y = 499500*2/(y+x+1) + x
    # b = 499500*2/(y+x+1) + x + 1/2
    # 2*(b-x-1/2) = 499500/(y+x+1) + 2*x
    # 2*(b-x-1/2) = 499500/(499500*2/(y+x+1) + x + 1) + 2*x
    # 2*(b-x-1/2) = (y+x+1)/(y+x+1) + 2*x
    # 2*(b-x-1/2) = (y+3*x+1)/(y+x+1)
    # 2*(b-x-1/2)*(y+x+1) = y+3*x+1
    # 2*(b-x-1/2)*(y+x+1) - y - 3*x = 1
    # 2*(b-x-1/2)*(y+x+1) - y - 3*x - 1 = 0
    # 2*(b-x-1/2)*(y+x+1) - y - 3*x - 1 - 2*(b-x-1/2)*(y+x+1) = - 2*(b-x-1/2)*(y+x+1)
    # 2*(b-x-1/2)*(y+x+1) - y - 3*x - 1 - 2*(b-x-1/2)*(y+x+1) + (y+x+1)^2 = - 2*(b-x-1/2)*(y+x+1) + (y+x+1)^2
    # 2*(b-x-1/2

=======
Suggestion 6

def calSnow(a, b):
    return int((b - a) * (b - a + 1) / 2 - a)

a, b = map(int, input().split())
print(calSnow(a, b))

=======
Suggestion 7

def snow(a,b):
    return b-a-1

a,b = map(int, input().split())
print(snow(a,b))

=======
Suggestion 8

def main():
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    print(b - a - 1)

=======
Suggestion 9

def calc(a, b):
    s = b - a
    x = int((2 * s + 0.25) ** 0.5 - 0.5)
    if x * (x + 1) < s:
        x += 1
    return x

=======
Suggestion 10

def solve(a,b):
    return sum(range(1,b-a+1))-a

print(solve(8,13))
print(solve(54,65))
