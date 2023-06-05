def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    # 移动棋子
    for i in range(q):
        for j in range(k):
            if l[j] < k and a[l[j]] < a[l[j] + 1]:
                a[l[j]] += 1
    # 打印结果
    for i in range(k):
        print(a[i], end=' ')
