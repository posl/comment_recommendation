def main():
    N = int(input())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
    # print(a)
    # print(b)
    # 1. 顶点编号为1,2,...,N。第i条边连接着顶点a_i和顶点b_i
    # 2. 判断这棵树是否是星形
    # 3. 星形是指有一个顶点直接连接到所有其他顶点的树
    # 4. 顶点直接连接到所有其他顶点的树，即除了一个顶点，其他顶点的度为1
    # 5. 那么，找出度为1的顶点，然后判断除了这个顶点外，其他顶点的度是否为1
    # 6. 建立一个数组，记录每个顶点的度
    degree = [0] * N
    for i in range(N-1):
        degree[a[i]-1] += 1
        degree[b[i]-1] += 1
    # print(degree)
    # 7. 找出度为1的顶点
    # 8. 如果度为1的顶点只有一个，那么这个顶点就是星形的中心
    center = -1
    for i in range(N):
        if degree[i] == 1:
            center = i
            break
    # print(center)
    # 9. 如果度为1的顶点有两个或两个以上，那么这个图不是星形
    if center == -1:
        print('No')
        exit()
    # 10. 除了中心顶点外，其他顶点的度是否为1
    for i in range(N-1):
        if a[i]-1 == center:
            degree[b[i]-1] -= 1
        elif b[i]-1 == center:
            degree[a[i]-1] -=
