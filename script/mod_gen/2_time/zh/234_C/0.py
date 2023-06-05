def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    max_len = 0
    for i in range(n):
        for j in range(i+1, n):
            max_len = max(max_len, len_two_points(points[i], points[j]))
    print(max_len)

if __name__ == '__main__':
    main()