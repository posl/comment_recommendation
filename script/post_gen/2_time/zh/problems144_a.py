Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a*b)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    if a <= 9 and b <= 9:
        print(a*b)
    else:
        print(-1)

=======
Suggestion 3

def main():
    # 读取输入
    # 用空格分割输入的字符串，然后转换成整数
    a, b = map(int, input().split())
    # 如果a和b都在1到9之间，那么打印a×b
    if a >= 1 and a <= 9 and b >= 1 and b <= 9:
        print(a * b)
    # 否则，打印-1
    else:
        print(-1)

main()

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        print("-1")
    else:
        print(a*b)

=======
Suggestion 5

def main():
    # 读取输入
    s = input().split(" ")
    a = int(s[0])
    b = int(s[1])
    # 输出结果
    if a <= 9 and b <= 9:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a < 1 or a > 20 or b < 1 or b > 20:
        return
    print(a * b)

main()
