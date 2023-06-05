def main():
    N = int(input())
    A = [0] * (N - 1)
    B = [0] * (N - 1)
    for i in range(N - 1):
        A[i], B[i] = map(int, input().split())
    # 每个顶点的度数
    degree = [0] * N
    for i in range(N - 1):
        degree[A[i] - 1] += 1
        degree[B[i] - 1] += 1
    # 找到度数为N-1的顶点
    for i in range(N):
        if degree[i] == N - 1:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()