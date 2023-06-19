def main():
    #读取数据
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int, input().split())
        X.append(x)
        Y.append(y)
    #计算所有可能的三角形的面积，正负不一
    areas = []
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                area = (X[j]-X[i])*(Y[k]-Y[i]) - (Y[j]-Y[i])*(X[k]-X[i])
                areas.append(area)
    #计算正面积的三角形的个数
    cnt = 0
    for area in areas:
        if area > 0:
            cnt += 1
    #打印结果
    print(cnt)
