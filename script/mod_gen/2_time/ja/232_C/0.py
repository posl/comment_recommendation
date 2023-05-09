def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i+1, N):
            AB[i][j] = AB[j][i] = 0
            CD[i][j] = CD[j][i] = 0
    for i in range(M):
        AB[AB[i][0]-1][AB[i][1]-1] = 1
        CD[CD[i][0]-1][CD[i][1]-1] = 1
    for i in range(N):
        for j in range(i+1, N):
            AB[i][j] = AB[j][i] = 0
            CD[i][j] = CD[j][i] = 0
    if AB == CD:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()