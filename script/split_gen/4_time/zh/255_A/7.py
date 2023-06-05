def main():
    # 读取输入
    R, C = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(2)]
    # 算法
    print(A[R - 1][C - 1])
