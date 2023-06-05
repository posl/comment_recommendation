Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B = map(int,input().split())
    if B%A == 0:
        print(int(B/A))
    else:
        print(int(B/A)+1)

=======
Suggestion 2

def main():
    # 输入
    A, B = map(int, input().split())
    # 逻辑
    if B % A == 0:
        print(B // A)
    else:
        print(B // A + 1)

=======
Suggestion 3

def solution():
    A, B = map(int, input().split())
    if B == 1:
        return 0
    else:
        return (B - 1 + A - 2) // (A - 1)

print(solution())

=======
Suggestion 4

def main():
    A,B = map(int,input().split())
    if B%A == 0:
        print(B//A)
    else:
        print(B//A+1)

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    print((b-1)//(a-1))

=======
Suggestion 6

def main():
    # 读取数据
    a, b = map(int, input().split())
    # 计算最少电源条数
    if b % a == 0:
        print(b//a)
    else:
        print(b//a+1)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if b%a==0:
        print(int(b/a))
    else:
        print(int(b/a)+1)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if b == 1:
        print(0)
    else:
        if b % a == 0:
            print(b // a)
        else:
            print(b // a + 1)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    ans = 0
    for i in range(1,20):
        if a*i>=b:
            ans = i
            break
    print(ans)
