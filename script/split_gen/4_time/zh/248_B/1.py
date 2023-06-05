def main():
    import sys
    # 读取输入
    input = sys.stdin.readline
    a, b, k = map(int, input().split())
    # 初始化
    ans = 0
    # 计算
    while a < b:
        a *= k
        ans += 1
    # 输出结果
    print(ans)
