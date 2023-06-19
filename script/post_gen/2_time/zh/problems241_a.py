Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    #print(a)
    k = 0
    for i in range(1, 4):
        k = a[k]
    print(k)

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 3

def main():
    a = input().split()
    a = list(map(int, a))
    k = 0
    for i in range(10):
        k = a[k]
    print(k)

=======
Suggestion 4

def main():
    a = [int(x) for x in input().split()]
    b = 0
    for i in range(3):
        b = a[b]
    print(b)

=======
Suggestion 5

def f(a):
    x = 0
    for i in range(10):
        x = a[x]
    return x

=======
Suggestion 6

def main():
    a = input().split()
    a = [int(i) for i in a]
    for i in range(3):
        a = [a[j] for j in a]
    print(a[0])

=======
Suggestion 7

def main():
    a = raw_input().split(' ')
    a = map(int, a)
    b = a[0]
    for i in range(1, 11):
        b = a[b]
    print b

=======
Suggestion 8

def convert(k, a):
    return a[k]

=======
Suggestion 9

def main():
    a = raw_input().split()
    for i in range(10):
        a[i] = int(a[i])
    b = [0] * 10
    for i in range(10):
        b[a[i]] = i
    print b[0]

=======
Suggestion 10

def problem241_a():
    # 读取输入
    a = input().split(" ")
    # 转换成整数
    a = [int(i) for i in a]
    # 初始化
    k = 0
    # 循环3次
    for i in range(3):
        # 取出a_k
        k = a[k]
    # 输出
    print(k)
