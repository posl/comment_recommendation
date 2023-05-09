def main():
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(2**N):
        mask = []
        for j in range(N):
            if i >> j & 1:
                mask.append(1)
            else:
                mask.append(0)
        #print(mask)
        cnt = 0
        for j in range(N):
            if mask[j] == 1:
                cnt += len(S[j])
        if cnt == 0:
            continue
        cnt2 = 0
        for j in range(26):
            cnt3 = 0
            for k in range(N):
                if mask[k] == 1 and chr(j+97) in S[k]:
                    cnt3 += 1
            if cnt3 == K:
                cnt2 += 1
        if cnt2 > ans:
            ans = cnt2
    print(ans)
main()
