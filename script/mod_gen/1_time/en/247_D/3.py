def main():
    Q = int(input())
    ball = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(query[2]):
                ball.append(query[1])
        else:
            print(sum(ball[:query[1]]))
            del ball[:query[1]]

if __name__ == '__main__':
    main()