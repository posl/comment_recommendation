def main():
    N,D = map(int,input().split())
    walls = []
    for i in range(N):
        L,R = map(int,input().split())
        walls.append([L,R])
    walls.sort()
    ans = 0
    for i in range(N):
        if walls[i][0] >= 0:
            ans += 1
            walls[i][0] = -1
            for j in range(i+1,N):
                if walls[j][0] >= 0:
                    if walls[j][0] <= walls[i][1]+D:
                        walls[j][0] = -1
                    else:
                        break
    print(ans)

if __name__ == '__main__':
    main()