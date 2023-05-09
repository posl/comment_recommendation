def main():
    N = int(input())
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split())))
    #print(xy)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                #print(xy[i], xy[j], xy[k])
                if (xy[j][1] - xy[i][1])*(xy[k][0] - xy[j][0]) == (xy[j][0] - xy[i][0])*(xy[k][1] - xy[j][1]):
                    print("Yes")
                    return
    print("No")
    return
