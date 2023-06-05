def main():
    N = int(input())
    point_list = []
    for i in range(N):
        point = input().split()
        point_list.append(point)
    #print(point_list)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1 = int(point_list[i][0])
                y1 = int(point_list[i][1])
                x2 = int(point_list[j][0])
                y2 = int(point_list[j][1])
                x3 = int(point_list[k][0])
                y3 = int(point_list[k][1])
                #print(x1, y1, x2, y2, x3, y3)
                s = abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))
                #print(s)
                if s > 0:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()