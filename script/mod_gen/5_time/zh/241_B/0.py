def main():
    # 读入
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 处理
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] <= B[j]:
            i += 1
        j += 1
    # 输出
    if i == N:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()