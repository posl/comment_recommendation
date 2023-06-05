def main():
    #输入
    N = int(input())
    x = [0]*N
    y = [0]*N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    #处理
    #先求出所有的距离
    distance = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            distance[i][j] = abs(x[i]-x[j]) + abs(y[i]-y[j])
            distance[j][i] = distance[i][j]
    #求出距离的最大值
    max_distance = 0
    for i in range(N):
        for j in range(i+1, N):
            if distance[i][j] > max_distance:
                max_distance = distance[i][j]
    #输出
    print(max_distance)
