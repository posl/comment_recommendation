def main():
    #读取输入
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    #计算最短距离
    min_dist = K
    for i in range(N):
        if i == N - 1:
            dist = K - A[i] + A[0]
        else:
            dist = A[i + 1] - A[i]
        if dist < min_dist:
            min_dist = dist
    #打印输出
    print(K - min_dist)
