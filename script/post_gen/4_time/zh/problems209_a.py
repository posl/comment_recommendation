Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b - a + 1)

=======
Suggestion 2

def solve():
    a,b = map(int,input().split())
    if a > b:
        print(0)
    else:
        print(b-a+1)

=======
Suggestion 3

def main():
    a = int(input("输入a:"))
    b = int(input("输入b:"))
    if a < 1 or a > 100 or b < 1 or b > 100:
        print("输入的a,b不在范围内")
        return
    if a > b:
        print("输入的a大于b,不符合要求")
        return
    print(b - a + 1)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    print(b-a+1) if a <= b else print(0)

=======
Suggestion 5

def problem209_a():
    a,b = map(int,input().split())
    print(b-a+1 if a<=b else 0)

=======
Suggestion 6

def count_ints(a,b):
    #a,b = input().split()
    #a = int(a)
    #b = int(b)
    count = 0
    for i in range(a,b+1):
        count += 1
    return count

=======
Suggestion 7

def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算结果
    ans = 0
    for i in range(a, b+1):
        ans += 1
    # 打印结果
    print(ans)
    return

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    print(b-a+1 if b-a >= 0 else 0)
