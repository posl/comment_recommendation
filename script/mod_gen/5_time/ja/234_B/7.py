def main():
    N = int(input())
    points = []
    max_len = 0
    for _ in range(N):
        points.append(tuple(map(int, input().split())))
    for i in range(N):
        for j in range(i+1, N):
            len = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
            if len > max_len:
                max_len = len
    print(max_len**0.5)

if __name__ == '__main__':
    main()