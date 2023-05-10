def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2**N):
        tmp = []
        for j in range(N):
            if (i>>j)&1:
                tmp.append(S[j])
        if len(tmp) != K:
            continue
        cnt = 0
        for k in range(26):
            for l in tmp:
                if chr(ord('a')+k) in l:
                    cnt += 1
                    break
        ans = max(ans, cnt)
    print(ans)
