def solve():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 用于计数的数组
    B = [0] * 200
    # 遍历输入，计数
    for a in A:
        B[a % 200] += 1
    # 计算答案
    ans = 0
    for b in B:
        ans += b * (b - 1) // 2
    # 输出答案
    print(ans)

if __name__ == '__main__':
    solve()