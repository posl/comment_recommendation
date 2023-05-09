def main():
    N, M, T = map(int, input().split())
    cafe = [list(map(int, input().split())) for _ in range(M)]
    cafe.append([T, T])
    battery = N
    time = 0
    for i in range(M+1):
        battery -= cafe[i][0] - time
        if battery <= 0:
            print("No")
            exit()
        battery += cafe[i][1] - cafe[i][0]
        battery = min(battery, N)
        time = cafe[i][1]
    print("Yes")

if __name__ == '__main__':
    main()