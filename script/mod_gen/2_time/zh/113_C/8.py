def main():
    N, M = map(int, input().split())
    P_Y = []
    for i in range(M):
        P_Y.append(list(map(int, input().split())))
    P_Y.sort(key=lambda x: x[1])
    ID = []
    for i in range(M):
        ID.append([P_Y[i][0], i+1, 1])
    ID.sort(key=lambda x: x[0])
    for i in range(M):
        ID[i][2] = str(ID[i][1]).zfill(6)
        ID[i][0] = str(ID[i][0]).zfill(6)
    for i in range(M):
        print(ID[i][0] + ID[i][2])

if __name__ == '__main__':
    main()