def main():
    N = int(input())
    a = list(map(int, input().split()))
    # 初期状態
    balls = []
    for i in range(N):
        balls.append(0)
    # ボールを落とす
    for i in range(N):
        balls[a[i]-1] += 1
    # 筒の中に何個のボールがあるか求める
    for i in range(N):
        print(balls[i])

if __name__ == '__main__':
    main()