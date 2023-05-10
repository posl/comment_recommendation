def main():
    #入力
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append([x, y])
    #処理
    max_dist = 0
    for i in range(N-1):
        for j in range(i+1, N):
            dist = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
            if dist > max_dist:
                max_dist = dist
    #出力
    print(max_dist**0.5)

if __name__ == '__main__':
    main()