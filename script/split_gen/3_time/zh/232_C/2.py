def get_ball_list(n, m, a_list, b_list):
    ball_list = []
    for i in range(1, n+1):
        ball = []
        for j in range(m):
            if i == a_list[j]:
                ball.append(b_list[j])
            elif i == b_list[j]:
                ball.append(a_list[j])
        ball_list.append(ball)
    return ball_list
