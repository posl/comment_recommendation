def main():
    N, M, Q = map(int, input().split())
    trains = [set() for _ in range(N)]
    for _ in range(M):
        L, R = map(int, input().split())
        trains[L-1].add(R)
    for i in range(1, N):
        trains[i] |= trains[i-1]
    for _ in range(Q):
        p, q = map(int, input().split())
        print(len(trains[q-1] & set(range(p, q))))

if __name__ == '__main__':
    main()