def main():
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    balls = []
    for query in queries:
        if query[0] == 1:
            balls += [query[1]] * query[2]
        else:
            print(sum(balls[:query[1]]))
            balls = balls[query[1]:]
