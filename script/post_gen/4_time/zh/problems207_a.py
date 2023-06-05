Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(max(a+b, b+c, c+a))

=======
Suggestion 2

def main():
    # 读取输入
    line = input()
    # 用空格分割输入
    s = line.split()
    # 将输入转换为整数
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    # 计算答案
    ans = a + b + c
    # 打印答案
    print(ans)

=======
Suggestion 3

def main():
    a = input().split()
    print(int(max(a))*2)

=======
Suggestion 4

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 计算结果
    ans = max(a+b, b+c, c+a)
    # 打印结果
    print(ans)

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    print(a+b+c)

=======
Suggestion 6

def main():
    # 读取输入
    # 用空格分割读取的字符串，转换成整数
    # 用list保存输入的整数
    a, b, c = map(int, input().split())
    # 用list保存输入的整数
    cards = [a, b, c]
    # 用sum函数求和
    print(sum(cards))

=======
Suggestion 7

def main():
    # 读入数据
    a, b, c = map(int, input().split())

    # 计算答案
    ans = a + b + c
    ans = max(ans, a + b)
    ans = max(ans, b + c)
    ans = max(ans, c + a)

    # 打印答案
    print(ans)

main()

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    print(max(a+b, b+c, a+c))

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    max = a+b+c
    if max < a+b:
        max = a+b
    if max < a+c:
        max = a+c
    if max < b+c:
        max = b+c
    print(max)
