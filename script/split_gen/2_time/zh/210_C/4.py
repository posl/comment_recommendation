def main():
    # 读取输入
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    # 求解
    ans = 0
    s = set()
    for i in range(n-k+1):
        for j in range(k):
            s.add(c[i+j])
        ans = max(ans, len(s))
        s.clear()
    # 输出
    print(ans)
