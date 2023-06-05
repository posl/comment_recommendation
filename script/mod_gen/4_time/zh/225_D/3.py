def main():
    N, Q = map(int, input().split())
    cars = [[] for _ in range(N+1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            cars[query[2]].extend(cars[query[1]])
            cars[query[1]] = []
        elif query[0] == 2:
            cars[query[1]].extend(cars[query[2]])
            cars[query[2]] = []
        else:
            print(' '.join(map(str, cars[query[1]])))

if __name__ == '__main__':
    main()