def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 从后往前遍历
    ans = []
    for i in range(n-1, -1, -1):
        ans.insert(a[i]-1, i+1)
    # 输出
    print(*ans)
