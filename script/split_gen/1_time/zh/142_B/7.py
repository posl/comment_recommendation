def main():
    # 读取输入
    n,k = map(int, input().split())
    h = list(map(int, input().split()))
    # 初始化
    ans = 0
    # 遍历
    for i in h:
        if i >= k:
            ans += 1
    # 输出结果
    print(ans)
