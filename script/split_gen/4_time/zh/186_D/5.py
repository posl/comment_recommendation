def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 计算答案
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += abs(a[i] - a[j])
    # 打印答案
    print(ans)
