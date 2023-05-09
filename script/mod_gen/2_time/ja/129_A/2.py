def main():
    # 入力
    P, Q, R = map(int, input().split())
    # 出力
    print(min(P + Q, Q + R, R + P))

if __name__ == '__main__':
    main()