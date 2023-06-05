def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 初始化
    a.sort()
    a.reverse()
    # 计算
    if sum(a) <= n:
        print(0)
    else:
        for i in range(m):
            if sum(a) - a[i] <= n:
                print(i + 1)
                break
        else:
            print(-1)
