def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: x[1])
    city = [0 for _ in range(N + 1)]
    for i in range(M):
        city[P_Y[i][0]] += 1
        P_Y[i].append(city[P_Y[i][0]])
    P_Y.sort()
    for i in range(M):
        print(str(P_Y[i][0]).zfill(6) + str(P_Y[i][3]).zfill(6))

if __name__ == '__main__':
    main()