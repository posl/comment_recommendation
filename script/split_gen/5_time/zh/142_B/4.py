def main():
    # 读取输入
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    # 计算结果
    ans = 0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    # 输出结果
    print(ans)
