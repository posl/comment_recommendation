def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    # print(query)
    ball = []
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                ball.append(query[i][1])
        else:
            print(sum(ball[:query[i][1]]))
            ball = ball[query[i][1]:]
