def main():
    N,K = map(int,input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2**26):
        cnt = 0
        for j in range(N):
            tmp = 0
            for k in range(26):
                if (i>>k)&1:
                    if chr(97+k) in S[j]:
                        tmp += 1
            if tmp >= K:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)
