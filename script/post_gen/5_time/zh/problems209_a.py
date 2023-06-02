Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def count(a,b):
    if a>b:
        return 0
    else:
        return b-a+1

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(B - A + 1 if B - A >= 0 else 0)

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    print(b-a+1 if b>a else 0)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(max(0, b - a + 1))

=======
Suggestion 5

def main():
    a,b=map(int,input().split())
    count=0
    for i in range(a,b+1):
        count+=1
    print(count)

=======
Suggestion 6

def countNums(a,b):
    count = 0
    for i in range(a,b+1):
        count += 1
    return count

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a > b:
        print(0)
    else:
        print(b-a+1)

=======
Suggestion 8

def count_integers(a,b):
    # a,b = input("please input two numbers:").split()
    # a = int(a)
    # b = int(b)
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return b-a+1

=======
Suggestion 9

def main():
    # 读取输入
    a, b = map(int, input().split())
    # 初始化答案
    ans = 0
    # 遍历所有的整数
    for i in range(1, 101):
        # 如果整数的范围在a和b之间
        if a <= i and i <= b:
            # 答案+1
            ans += 1
    # 输出答案
    print(ans)
