def main():
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    balls = []
    for i in range(Q):
        if queries[i][0] == 1:
            for _ in range(queries[i][2]):
                balls.append(queries[i][1])
        elif queries[i][0] == 2:
            print(sum(balls[:queries[i][1]]))

if __name__ == '__main__':
    main()