def solve():
    # 从标准输入读取
    A, B, C = map(int, input().split())
    # 解决问题
    if C == 0:
        if A > B:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if A < B:

if __name__ == '__main__':
    solve()