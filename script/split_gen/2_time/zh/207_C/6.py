def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int,input().split())))
    count = 0
    for i in range(0,N):
        for j in range(i+1,N):
            if tlr[i][1] <= tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                count += 1
            elif tlr[i][1] <= tlr[j][2] and tlr[j][2] <= tlr[i][2]:
                count += 1
            elif tlr[j][1] <= tlr[i][1] and tlr[i][1] <= tlr[j][2]:
                count += 1
            elif tlr[j][1] <= tlr[i][2] and tlr[i][2] <= tlr[j][2]:
                count += 1
    print(count)
