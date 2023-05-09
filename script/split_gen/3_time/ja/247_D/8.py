def main():
    Q = int(input())
    querys = [list(map(int, input().split())) for _ in range(Q)]
    # print(querys)
    balls = []
    for query in querys:
        if query[0] == 1:
            balls.extend([query[1]] * query[2])
        elif query[0] == 2:
            print(sum(balls[:query[1]]))
