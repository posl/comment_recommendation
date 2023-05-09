def main():
    n, q = map(int, input().split())
    # ボールを並べる
    balls = [i for i in range(1, n + 1)]
    # ボールの位置を記録する
    ball_pos = [i for i in range(n)]
    for _ in range(q):
        x = int(input())
        # ボールを入れ替える
        # ボールの位置を記録する
        balls[ball_pos[x - 1]], balls[ball_pos[x - 1] + 1] = balls[ball_pos[x - 1] + 1], balls[ball_pos[x - 1]]
        ball_pos[x - 1], ball_pos[x - 1] + 1 = ball_pos[x - 1] + 1, ball_pos[x - 1]
        # ボールの位置を記録する
        if ball_pos[x - 1] == n - 1:
            ball_pos[x - 1] = 0
        else:
            ball_pos[x - 1] += 1
    print(*balls)

if __name__ == '__main__':
    main()