def main():
    N, M, Q = map(int, input().split())
    trains = []
    for i in range(M):
        trains.append(list(map(int, input().split())))
    trains.sort()
    for i in range(Q):
        p, q = map(int, input().split())
        count = 0
        for j in range(M):
            if trains[j][0] >= p and trains[j][1] <= q:
                count += 1
        print(count)

if __name__ == '__main__':
    main()