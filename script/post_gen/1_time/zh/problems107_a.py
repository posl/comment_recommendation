Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    str = input("输入N i：")
    strlist = str.split()
    N = int(strlist[0])
    i = int(strlist[1])
    j = N - i + 1
    print(j)

=======
Suggestion 2

def main():
    N,i = map(int,input().split())
    print(N+1-i)

=======
Suggestion 3

def main():
    N,i = map(int,input().split())
    print(N-i+1)

=======
Suggestion 4

def main():
    #N i
    N,i = input().split()
    N = int(N)
    i = int(i)
    print(N-i+1)

=======
Suggestion 5

def main():
    n,i = map(int,input().split())
    print(n-i+1)

=======
Suggestion 6

def solve(n, i):
    return n - i + 1

=======
Suggestion 7

def main():
    # 读取输入
    n, i = map(int, input().split())

    # 计算
    j = n - i + 1

    # 打印输出
    print(j)

=======
Suggestion 8

def get_j(n,i):
    return n+1-i
