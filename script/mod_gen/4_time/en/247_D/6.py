def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    balls = []
    num = 0
    for i in range(Q):
        if query[i][0] == 1:
            balls.append(query[i][1])
            num += query[i][2]
        else:
            print(sum(balls[:query[i][1]]) + num)
            balls = balls[query[i][1]:]

if __name__ == '__main__':
    main()