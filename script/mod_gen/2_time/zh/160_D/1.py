def main():
    # 读入数据
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 计算距离
    A.append(K)
    A.append(K + A[0])
    A.sort()
    # print(A)
    dist = [A[i] - A[i - 1] for i in range(1, N + 2)]
    # print(dist)
    print(K - max(dist))

if __name__ == '__main__':
    main()