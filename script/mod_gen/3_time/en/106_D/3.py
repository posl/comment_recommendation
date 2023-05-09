def main():
    N, M, Q = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for q in queries:
        print(sum([1 for t in trains if q[0] <= t[0] and t[1] <= q[1]]))

if __name__ == '__main__':
    main()