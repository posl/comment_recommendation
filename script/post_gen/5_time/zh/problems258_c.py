Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[-x:] + S[:-x]
        else:
            print(S[x-1])

=======
Suggestion 2

def main():
    # 读取输入
    n, q = map(int, input().split())
    s = input()
    # 以列表形式存储
    s = list(s)
    # 处理查询
    for i in range(q):
        t, x = map(str, input().split())
        x = int(x)
        if t == '1':
            # 1 x:连续执行以下x次：删除S的最后一个字符并将其附加到开头。
            for j in range(x):
                s.insert(0, s.pop())
        elif t == '2':
            # 2 x:打印S的第x个字符。
            print(s[x - 1])

=======
Suggestion 3

def main():
    n,q = map(int,input().split())
    s = input()
    s = list(s)
    for _ in range(q):
        t,x = map(int,input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])

=======
Suggestion 4

def solve():
    # 读入数据
    n, q = map(int, input().split())
    s = input()
    query = [list(map(int, input().split())) for _ in range(q)]

    # 处理
    # 1.找到第一个被移动的字符位置
    # 2.找到该字符被移动后的位置
    # 3.根据移动的次数和字符移动后的位置，计算出字符移动后的位置
    # 4.根据移动后的位置，找到原来的字符
    # 5.输出
    # 6.重复1-5
    for t, x in query:
        x = x - 1
        for _ in range(x):
            if s[x] == s[x - 1]:
                x -= 1
            else:
                break
        x = (x - t) % n
        print(s[x])

=======
Suggestion 5

def main():
    # 将输入的字符串转换为列表
    N, Q = map(int, input().split())
    S = list(input())
    # 依次处理Q个查询
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            # 1 x:连续执行以下x次：删除S的最后一个字符并将其附加到开头。
            S = S[-x:] + S[:-x]
        else:
            # 2 x:打印S的第x个字符。
            print(S[x - 1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[N-x:] + S[:N-x]
        else:
            print(S[x-1])

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[n-x:] + s[:n-x]
        else:
            print(s[x-1])

=======
Suggestion 8

def main():
    # 读取输入
    n, q = map(int, input().split())
    s = input()
    # 处理
    for i in range(q):
        # 读取输入
        t, x = map(int, input().split())
        if t == 2:
            # 输出
            print(s[x - 1])
        else:
            # 处理
            s = s[-x:] + s[:-x]

=======
Suggestion 9

def shift_string(s, n):
    return s[n:] + s[:n]

=======
Suggestion 10

def main():
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])
