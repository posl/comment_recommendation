def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    # 棋子位置
    p = [0] * n
    for i in range(k):
        p[a[i] - 1] += 1
    # print(p)
    # 棋子移动
    for i in range(q):
        for j in range(k):
            if p[a[l[j] - 1] - 1] == 1:
                break
            if a[l[j] - 1] == n:
                continue
            p[a[l[j] - 1] - 1] -= 1
            p[a[l[j] - 1]] += 1
            a[l[j] - 1] += 1
        # print(p)
    # print(a)
    # print(l)
    # 输出
    for i in range(k):
        print(a[l[i] - 1], end=' ')
