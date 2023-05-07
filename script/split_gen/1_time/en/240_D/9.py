def check_balls(balls):
    if len(balls) < 2:
        return balls
    else:
        if balls[-1] == balls[-2]:
            balls = balls[:-2]
            return check_balls(balls)
        else:
            return balls
n = int(input())
balls = []
for i in range(n):
    balls.append(int(input()))
    balls = check_balls(balls)
    print(len(balls))
