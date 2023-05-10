def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = input().split()
        points.append((int(x), int(y)))
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (points[i][0] - points[j][0]) * (points[i][1] - points[k][1]) == (points[i][0] - points[k][0]) * (points[i][1] - points[j][1]):
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()