def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    #print(N, M)
    #print(S)
    #print(T)
    # 末尾3文字が一致するものの数をカウント
    cnt = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()