def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append([int(x) for x in input().split()])
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if (points[i][0] - points[j][0]) * (points[i][1] - points[k][1]) == (points[i][0] - points[k][0]) * (points[i][1] - points[j][1]):
                    print('Yes')
                    return
    print('No')
    return

if __name__ == '__main__':
    main()