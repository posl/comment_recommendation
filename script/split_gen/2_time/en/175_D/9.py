def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**20
    for i in range(N):
        tmp = 0
        cnt = 0
        j = i
        while cnt < K:
            tmp += C[P[j]-1]
            if tmp > ans:
                ans = tmp
            j = P[j]-1
            cnt += 1
            if j == i:
                break
        if cnt == K:
            continue
        else:
            if tmp <= 0:
                continue
            else:
                tmp *= (K-cnt)//cnt
                if tmp > ans:
                    ans = tmp
                tmp = 0
                cnt = 0
                j = i
                while cnt < (K-cnt)%cnt:
                    tmp += C[P[j]-1]
                    if tmp > ans:
                        ans = tmp
                    j = P[j]-1
                    cnt += 1
                    if j == i:
                        break
    print(ans)
main()
