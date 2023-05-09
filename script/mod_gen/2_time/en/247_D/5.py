def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    balls = []
    sum = 0
    for i in range(Q):
        if queries[i][0] == 1:
            for j in range(queries[i][2]):
                balls.append(queries[i][1])
        elif queries[i][0] == 2:
            for j in range(queries[i][1]):
                sum += balls[j]
            print(sum)
            sum = 0
            del balls[:queries[i][1]]

if __name__ == '__main__':
    main()