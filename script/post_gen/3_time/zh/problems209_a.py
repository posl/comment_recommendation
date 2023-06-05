Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    A, B = map(int, input().split())
    #初始化计数器
    count = 0
    # 遍历整数
    for i in range(A, B + 1):
        # 如果是整数，计数器加1
        count += 1
    # 打印计数器
    print(count)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(B - A + 1) if A <= B else print(0)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(b - a + 1 if b - a + 1 > 0 else 0)

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    print(b-a+1 if b>=a else 0)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(b-a+1 if b-a>=0 else 0)

=======
Suggestion 6

def main():
    # 读取输入
    A, B = map(int, input().split())

    # 用来计数的变量
    count = 0

    # 在这里写下你的代码
    for x in range(A, B + 1):
        if A <= x <= B:
            count += 1

    # 输出结果
    print(count)

=======
Suggestion 7

def cal(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += 1
    return sum

a,b = input().split()
print(cal(int(a),int(b)))

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    print(B - A + 1 if B >= A else 0)

=======
Suggestion 9

def main():
    A,B = map(int,input().split())
    if A <= B:
        print(B-A+1)
    else:
        print(0)
