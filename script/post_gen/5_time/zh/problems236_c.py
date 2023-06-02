Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = list(map(str, input().split()))
    t = list(map(str, input().split()))
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()

    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    s = list(input().split())
    t = list(input().split())
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def solve():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    # 读入数据
    n, m = list(map(int, input().split()))
    s = input().split()
    t = input().split()
    # 生成一个字典，键为车站名，值为是否停靠
    t_dict = {}
    for i in range(m):
        t_dict[t[i]] = True
    for i in range(n):
        if s[i] in t_dict:
            print("Yes")
        else:
            print("No")
