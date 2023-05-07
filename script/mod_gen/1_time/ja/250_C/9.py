def main():
    N, Q = map(int, input().split())
    # 0 で初期化
    balls = [0] * N
    # 1 から N まで代入
    for i in range(N):
        balls[i] = i + 1
    # 操作
    for i in range(Q):
        x = int(input())
        # 交換
        balls[x - 1], balls[x] = balls[x], balls[x - 1]
    # 出力
    for i in range(N):
        print(balls[i], end = " ")

if __name__ == '__main__':
    main()