def get_num_balls_per_color(N, M, cylinder):
    num_balls_per_color = [0] * N
    for i in range(M):
        for j in range(cylinder[i][0]):
            num_balls_per_color[cylinder[i][1 + j] - 1] += 1
    return num_balls_per_color

if __name__ == '__main__':
    get_num_balls_per_color()