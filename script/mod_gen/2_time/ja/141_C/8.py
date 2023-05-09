def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    # 参加者のポイント
    point = [K - Q] * N
    # 正解した参加者のポイントを1増やす
    for a in A:
        point[a - 1] += 1
    # ポイントが0以下の参加者は敗退
    for p in point:
        if p > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()