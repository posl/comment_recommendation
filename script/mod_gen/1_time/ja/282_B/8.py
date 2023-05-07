def main():
    #入力
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    #print(N, M)
    #print(S)
    # 答えを出力
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                if S[i][k] == 'o' or S[j][k] == 'o':
                    count += 1
                    break
    print(count)

if __name__ == '__main__':
    main()