Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def g_1(x):
    y = str(x)
    y = list(y)
    y.sort(reverse=True)
    y = ''.join(y)
    y = int(y)
    return y

=======
Suggestion 2

def g1(x):
    return int(''.join(sorted(str(x),reverse=True)))

=======
Suggestion 3

def f(x):
    g1 = int(''.join(sorted(str(x), reverse=True)))
    g2 = int(''.join(sorted(str(x))))
    return g1 - g2

N, K = map(int, input().split())

for i in range(K):
    N = f(N)
print(N)

=======
Suggestion 4

def g_1(x):
    a = []
    while x != 0:
        a.append(x % 10)
        x = x // 10
    a.sort(reverse=True)
    b = ''.join(str(i) for i in a)
    return int(b)

=======
Suggestion 5

def g_1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = ''.join(x)
    return int(x)

=======
Suggestion 6

def g_1(x):
    #将x的十进制数字按降序重新排列而得到的整数
    x = str(x)
    x = sorted(x,reverse=True)
    x = ''.join(x)
    x = int(x)
    return x

=======
Suggestion 7

def f(x):
    return g1(x)-g2(x)

=======
Suggestion 8

def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = ''.join(x)
    return int(x)

=======
Suggestion 9

def g_1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = ''.join(x)
    x = int(x)
    return x
