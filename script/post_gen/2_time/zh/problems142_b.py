Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    print(len([i for i in h if i >= k]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    count = 0
    for i in h:
        if i >= k:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)

main()

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    # 读取数据
    N, K = map(int, input().split())
    h = [int(i) for i in input().split()]

    # 计算
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1

    # 输出结果
    print(count)

=======
Suggestion 7

def main():
    # 读取输入
    num, height = map(int, input().split())
    heights = list(map(int, input().split()))
    # 计算
    count = 0
    for h in heights:
        if h >= height:
            count += 1
    # 打印结果
    print(count)

=======
Suggestion 8

def main():
    # 获取输入
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    # 处理
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    # 输出
    print(count)
