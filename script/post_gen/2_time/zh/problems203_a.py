Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    while True:
        try:
            a, b, c = input().split()
            a = int(a)
            b = int(b)
            c = int(c)
            if 1 <= a <= 6 and 1 <= b <= 6 and 1 <= c <= 6:
                return a, b, c
            else:
                print("输入错误，请重新输入")
        except:
            print("输入错误，请重新输入")

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if a==b:
        print(c)
    elif a==c:
        print(b)
    elif b==c:
        print(a)
    else:
        print(0)

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if a==b:
        print(c)
    elif b==c:
        print(a)
    elif c==a:
        print(b)
    else:
        print(0)

=======
Suggestion 4

def main():
    a,b,c = map(int, input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)

main()

=======
Suggestion 5

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 处理
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)
