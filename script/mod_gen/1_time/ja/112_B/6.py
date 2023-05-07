def main():
    # 入力
    N, T = map(int, input().split())
    c = [0] * N
    t = [0] * N
    for i in range(N):
        c[i], t[i] = map(int, input().split())
    # 処理
    ans = 1001
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])
    # 出力
    if ans != 1001:
        print(ans)
    else:
        print("TLE")

if __name__ == '__main__':
    main()