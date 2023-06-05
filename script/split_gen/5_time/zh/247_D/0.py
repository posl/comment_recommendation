def main():
    Q = int(input())
    querys = []
    for i in range(Q):
        querys.append(input())
    balls = []
    for query in querys:
        if query[0] == '1':
            balls.append(query[2:])
        else:
            n = int(query[2:])
            for i in range(n):
                balls.pop(0)
            print(sum([int(ball) for ball in balls]))
