def main():
    # 读取输入
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    # 交换
    B = A[:P-1] + A[R-1:S] + A[Q-1:R-1] + A[S:]
    # 打印输出
    print(' '.join(map(str, B)))
