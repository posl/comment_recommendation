def main():
    q = int(input())
    balls = []
    ball_sum = 0
    min_ball = 10**9
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            balls.append(query[1])
            ball_sum += query[1]
            if min_ball > query[1]:
                min_ball = query[1]
        elif query[0] == 2:
            ball_sum += query[1] * len(balls)
            min_ball += query[1]
        elif query[0] == 3:
            print(min_ball)
            ball_sum -= min_ball
            min_ball = 10**9
            if len(balls) > 0:
                min_ball = min(balls)
    return

if __name__ == '__main__':
    main()