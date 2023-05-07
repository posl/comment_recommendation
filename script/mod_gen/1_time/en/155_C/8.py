def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = sorted(S)
    #print(S)
    cnt = 1
    max_cnt = 0
    max_S = []
    for i in range(1, N):
        if S[i-1] == S[i]:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                max_S = [S[i-1]]
            elif cnt == max_cnt:
                max_S.append(S[i-1])
            cnt = 1
    if cnt > max_cnt:
        max_S = [S[N-1]]
    elif cnt == max_cnt:
        max_S.append(S[N-1])
    for s in max_S:
        print(s)

if __name__ == '__main__':
    main()