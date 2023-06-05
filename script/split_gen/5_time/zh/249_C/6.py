def main():
    # 读入
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    # 位运算
    ans = 0
    for i in range(1 << n):
        t = set()
        for j in range(n):
            if (i >> j) & 1:
                t |= set(s[j])
        if len(t) == k:
            ans = max(ans, bin(i).count("1"))
    # 输出
    print(ans)
