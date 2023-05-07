def main():
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    balls = []
    balls.append(0)
    balls.append(0)
    add = 0
    for i in range(Q):
        if query[i][0] == 1:
            balls.append(query[i][1] - add)
        elif query[i][0] == 2:
            add += query[i][1]
        else:
            min_value = min(balls)
            print(min_value + add)
            balls.remove(min_value)
