def main():
    N = int(input())
    xy = []
    for i in range(N):
        x, y = map(int, input().split())
        xy.append((x, y))
    max_dist = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = ((xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2)**0.5
            if dist > max_dist:
                max_dist = dist
    print(max_dist)

if __name__ == '__main__':
    main()