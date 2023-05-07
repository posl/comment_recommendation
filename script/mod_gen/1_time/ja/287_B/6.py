def main():
    # 入力
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    # 出力
    for i in range(N):
        ans = 0
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()