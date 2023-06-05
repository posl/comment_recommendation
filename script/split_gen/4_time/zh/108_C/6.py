def main():
    # 读取输入
    n, k = map(int, input().split())
    # 定义变量
    ans = 0
    # 计算
    for a in range(1, n + 1):
        ans += (n // a) * max(0, a - k)
        ans += max(0, (n % a + 1) - k) if k > 0 else 0
    # 输出
    print(ans)
