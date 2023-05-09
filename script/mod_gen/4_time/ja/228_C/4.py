def main():
    n, k = map(int, input().split())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    points.sort(key=lambda x: x[2], reverse=True)
    points.sort(key=lambda x: x[1], reverse=True)
    points.sort(key=lambda x: x[0], reverse=True)
    for i in range(n):
        if points[i][0] == points[k-1][0] and points[i][1] == points[k-1][1] and points[i][2] == points[k-1][2]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()