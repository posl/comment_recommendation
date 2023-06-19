Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem125_a():
    a, b, t = map(int, input().split())
    print((t // a) * b)

=======
Suggestion 2

def problem125_a():
    a,b,t = map(int, input().split())
    count = 0
    for i in range(1,t+1):
        if i % a == 0:
            count += b
    print(count)

=======
Suggestion 3

def solve():
    A, B, T = map(int, input().split())
    ans = 0
    for i in range(1, T+1):
        if i % A == 0:
            ans += B
    print(ans)

=======
Suggestion 4

def problems125_a():
    a,b,t = map(int,input().split())
    #print(a,b,t)
    count = 0
    for i in range(1,t+1):
        if i%a == 0:
            count += b
    print(count)

=======
Suggestion 5

def problem125_a():
    A,B,T = map(int, input().split())
    count = 0
    for i in range(1,T+1):
        if i%A == 0:
            count += B
    print(count)
problem125_a()

=======
Suggestion 6

def main():
    # 读取输入
    A,B,T = map(int, input().split())
    # 计算结果
    count = 0
    for i in range(1, T+1):
        if i % A == 0:
            count += B
    # 输出结果
    print(count)

=======
Suggestion 7

def main():
    A,B,T = map(int,input().split())
    count = 0
    for i in range(1,T+1):
        if i%A == 0:
            count += B
    print(count)

=======
Suggestion 8

def get_cookies(a,b,t):
    cookies = 0
    for i in range(1,t+1):
        if i % a == 0:
            cookies += b
    return cookies

=======
Suggestion 9

def main():
    a,b,t = map(int,input().split())
    count = 0
    for i in range(1,t+1):
        if i%a == 0:
            count += b
    print(count)
