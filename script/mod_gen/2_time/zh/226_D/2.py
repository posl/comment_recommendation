def main():
    N = int(input())
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split())))
    xy.sort(key=lambda x: x[0])
    #print(xy)
    xy2 = []
    for i in range(N):
        xy2.append([xy[i][0], xy[i][1]])
    xy2.sort(key=lambda x: x[1])
    #print(xy2)
    xy3 = []
    for i in range(N):
        xy3.append([xy2[i][0], xy2[i][1]])
    xy3.sort(key=lambda x: x[0])
    #print(xy3)
    xy4 = []
    for i in range(N):
        xy4.append([xy3[i][0], xy3[i][1]])
    xy4.sort(key=lambda x: x[1])
    #print(xy4)
    xy5 = []
    for i in range(N):
        xy5.append([xy4[i][0], xy4[i][1]])
    xy5.sort(key=lambda x: x[0])
    #print(xy5)
    xy6 = []
    for i in range(N):
        xy6.append([xy5[i][0], xy5[i][1]])
    xy6.sort(key=lambda x: x[1])
    #print(xy6)
    xy7 = []
    for i in range(N):
        xy7.append([xy6[i][0], xy6[i][1]])
    xy7.sort(key=lambda x: x[0])
    #print(xy7)
    xy8 = []
    for i in range(N):
        xy8.append([xy7[i][0], xy7[i][1]])
    xy8.sort(key=lambda x: x[1])
    #print(xy8)
    xy9 = []
    for i in range(N):
        xy9.append([xy8[i][0], xy8[i][1]])
    xy9.sort(key=lambda x: x[0])
    #print(xy9)
    xy10 = []
    for i in range(N):
        xy10.append([xy9[i][0], xy9[i][1]])
    xy10.sort(key=lambda x: x[1])
    #print(xy10)
    xy11 = []
    for i in range(N):
        xy11.append([xy10[i][0], xy10[i][1]])
    xy11.sort

if __name__ == '__main__':
    main()