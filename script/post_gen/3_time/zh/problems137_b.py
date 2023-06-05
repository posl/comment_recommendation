Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K, X = map(int, input().split())
    for i in range(X - K + 1, X + K):
        print(i, end=' ')

=======
Suggestion 2

def main():
    k,x = map(int,input().split())
    left = x-k+1
    right = x+k
    for i in range(left,right):
        print(i,end=" ")

=======
Suggestion 3

def main():
    # 读入数据
    k, x = map(int, input().split())

    # 计算结果
    result = list(range(x - k + 1, x + k))

    # 打印结果
    print(*result)

=======
Suggestion 4

def main():
    k, x = map(int, input().split())
    print(*[i for i in range(x-k+1, x+k)])

=======
Suggestion 5

def main():
    K, X = map(int, input().split())
    for i in range(X-K+1, X+K):
        print(i, end=' ')
    print(X+K)

=======
Suggestion 6

def solve(k, x):
    return range(x - k + 1, x + k)

=======
Suggestion 7

def solve():
    k, x = map(int, input().split())
    for i in range(x-k+1, x+k):
        print(i, end=' ')

solve()

=======
Suggestion 8

def problem137_b():
    pass

=======
Suggestion 9

def main():
    pass
