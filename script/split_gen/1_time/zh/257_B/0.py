def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    #初始化棋子位置
    x = [0] * n
    for i in range(k):
        x[a[i] - 1] = 1
    #执行棋子操作
    for i in range(q):
        for j in range(n - 1):
            if l[i] == j + 1 and x[j] == 1 and x[j + 1] == 0:
                x[j] = 0
                x[j + 1] = 1
    #输出棋子位置
    for i in range(n):
        if x[i] == 1:
            print(i + 1, end=" ")
    print()
