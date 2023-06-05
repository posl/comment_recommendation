def main():
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(1 << N):
        tmp = []
        for j in range(N):
            if (i >> j) & 1:
                tmp.append(S[j])
        if len(tmp) != K:
            continue
        cnt = 0
        for j in range(26):
            flag = True
            for k in range(K):
                if chr(j + 97) not in tmp[k]:
                    flag = False
            if flag:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
