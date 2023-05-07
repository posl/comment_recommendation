def main():
    N, D = map(int, input().split())
    wall = []
    for i in range(N):
        l, r = map(int, input().split())
        wall.append([l, r])
    wall.sort(key=lambda x: x[0])
    #print(wall)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if wall[j][0] - wall[i][1] <= D:
                count += 1
    print(count)

if __name__ == '__main__':
    main()