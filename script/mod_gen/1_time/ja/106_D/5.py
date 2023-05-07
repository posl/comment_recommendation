def main():
    n, m, q = map(int, input().split())
    trains = []
    for _ in range(m):
        l, r = map(int, input().split())
        trains.append((l, r))
    trains.sort()
    #print(trains)
    for _ in range(q):
        p, q = map(int, input().split())
        cnt = 0
        for train in trains:
            if p <= train[0] and train[1] <= q:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()