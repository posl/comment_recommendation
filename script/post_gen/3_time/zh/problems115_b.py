Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    print(int(sum(p) - p[-1]/2))

=======
Suggestion 2

def main():
    # 读取数据
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    # 处理
    p.sort()
    p[-1] = p[-1] / 2
    # 输出结果
    print(int(sum(p)))

=======
Suggestion 3

def main():
    n = input()
    p = []
    for i in range(int(n)):
        p.append(input())
    p.sort()
    p.reverse()
    p[0] = p[0] / 2
    print(int(sum(p)))

=======
Suggestion 4

def main():
    n = int(input())
    p = [int(input()) for i in range(n)]
    p.sort()
    p[-1] = int(p[-1]/2)
    print(sum(p))

=======
Suggestion 5

def solve():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    print(sum(p) - p[-1]//2)
solve()

=======
Suggestion 6

def main():
    n = int(input())
    price = []
    for i in range(n):
        price.append(int(input()))
    price.sort()
    price[n-1] = price[n-1] / 2
    print(int(sum(price)))

=======
Suggestion 7

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    p[-1] = int(p[-1] / 2)
    print(sum(p))

=======
Suggestion 8

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p[-1] = p[-1] / 2
    print(int(sum(p)))

=======
Suggestion 9

def get_input():
    N = int(raw_input())
    p = []
    for i in range(N):
        p.append(int(raw_input()))
    return N, p
