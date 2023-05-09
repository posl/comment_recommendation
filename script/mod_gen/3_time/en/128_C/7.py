def main():
    N,M = map(int,input().split())
    S = []
    P = []
    for i in range(M):
        S.append(list(map(int,input().split())))
    P = list(map(int,input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(1,len(S[j])):
                if (i >> (S[j][k]-1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()