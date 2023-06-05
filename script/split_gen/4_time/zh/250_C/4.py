def swap_ball(balls, i):
    tmp = balls[i]
    balls[i] = balls[i+1]
    balls[i+1] = tmp
    return balls
