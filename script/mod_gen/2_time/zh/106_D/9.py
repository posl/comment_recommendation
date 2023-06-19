def main():
    n,m,q = map(int, input().split())
    trains = []
    for _ in range(m):
        l,r = map(int, input().split())
        trains.append((l,r))
    for _ in range(q):
        p,q = map(int, input().split())
        count = 0
        for l,r in trains:
            if p <= l and r <= q:
                count += 1
        print(count)

if __name__ == '__main__':
    main()