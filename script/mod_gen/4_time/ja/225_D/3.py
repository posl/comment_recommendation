def main():
    N, Q = map(int, input().split())
    trains = [[i] for i in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1] - 1, query[2] - 1
            trains[x] += trains[y]
            trains[y] = []
        elif query[0] == 2:
            x, y = query[1] - 1, query[2] - 1
            trains[x] = [trains[x][0]] + trains[x][1:]
            trains[y] = trains[y] + [trains[y][0]]
        elif query[0] == 3:
            x = query[1] - 1
            print(*trains[x])

if __name__ == '__main__':
    main()