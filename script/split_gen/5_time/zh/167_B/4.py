def main():
    # 读取输入
    A, B, C, K = map(int, input().split())
    # 计算和
    ans = min(A, K)
    K -= A
    K = max(K, 0)
    K -= B
    ans -= min(C, K)
    # 输出结果
    print(ans)
