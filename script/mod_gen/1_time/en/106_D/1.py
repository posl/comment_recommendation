def main():
    N, M, Q = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    #print(trains)
    #print(queries)
    #print(N, M, Q)
    for p, q in queries:
        print(sum([1 for l, r in trains if l >= p and r <= q]))

if __name__ == '__main__':
    main()