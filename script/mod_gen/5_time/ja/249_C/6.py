def main():
    N,K = map(int,input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        cnt = 0
        tmp = []
        for j in range(N):
            if i & (1 << j):
                tmp.append(S[j])
        for k in range(26):
            flg = True
            for l in range(len(tmp)):
                if chr(k + ord('a')) not in tmp[l]:
                    flg = False
                    break
            if flg:
                cnt += 1
        if cnt == K:
            ans = max(ans,len(tmp))
    print(ans)

if __name__ == '__main__':
    main()