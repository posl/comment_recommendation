def main():
    # 读取输入
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 求出总和
    sum = 0
    for i in range(M):
        sum += A[i]
    # 判断
    if sum > N:
        print(-1)
    else:
        print(N - sum)
