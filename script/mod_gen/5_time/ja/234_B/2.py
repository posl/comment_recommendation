def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    max_len = 0.0
    for i in range(n):
        for j in range(i+1, n):
            x = points[i][0] - points[j][0]
            y = points[i][1] - points[j][1]
            length = (x**2 + y**2)**0.5
            if length > max_len:
                max_len = length
    print(max_len)

if __name__ == '__main__':
    main()