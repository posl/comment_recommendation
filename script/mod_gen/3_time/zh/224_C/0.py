def main():
    n = int(input())
    point = []
    for i in range(n):
        point.append(list(map(int,input().split())))
    #print(point)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (point[i][0] - point[k][0]) * (point[j][1] - point[k][1]) != (point[j][0] - point[k][0]) * (point[i][1] - point[k][1]):
                    count += 1
    print(count)

if __name__ == '__main__':
    main()