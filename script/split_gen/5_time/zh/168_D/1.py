def main():
    # 读入数据
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    # 从1号房间开始，通过通道移动到达的房间
    to = [[] for _ in range(n + 1)]
    for i in range(m):
        to[a[i]].append(b[i])
        to[b[i]].append(a[i])
    # 求解
    ans = [0] * (n + 1)
    ans[1] = 1
    for i in to[1]:
        ans[i] = 1
    for i in to[1]:
        for j in to[i]:
            if ans[j] == 0:
                ans[j] = i
    # 输出结果
    print("Yes")
    for i in range(2, n + 1):
        print(ans[i])
