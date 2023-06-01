Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    p, q, r = map(int, input().split())
    print(min(p+q, q+r, r+p))

=======
Suggestion 2

def min_time(p,q,r):
    return min(p+q, q+r, r+p)

=======
Suggestion 3

def main():
    # 获取输入
    p, q, r = map(int, input().split())

    # 计算最小时间
    min_time = p + q
    if min_time > q + r:
        min_time = q + r
    if min_time > r + p:
        min_time = r + p

    # 打印结果
    print(min_time)

=======
Suggestion 4

def main():
    p,q,r = map(int, input().split(' '))
    print(min(p+q, q+r, r+p))

=======
Suggestion 5

def main():
    # 读取输入
    p, q, r = map(int, input().split())
    # 计算最短时间
    print(min(p + q, q + r, r + p))
