def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    balls = []
    sum = 0
    for i in range(Q):
        if query[i][0] == 1:
            balls.append(query[i][1])
            sum += query[i][1] * query[i][2]
        else:
            for j in range(query[i][1]):
                sum -= balls.pop(0)
            print(sum)
