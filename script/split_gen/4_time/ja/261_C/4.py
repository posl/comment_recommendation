def main():
    N = int(input())
    S = [input() for _ in range(N)]
    cnt = {}
    for s in S:
        if s not in cnt:
            cnt[s] = 1
        else:
            cnt[s] += 1
    ans = []
    for i in range(N):
        if cnt[S[i]] == 1:
            ans.append(S[i])
        else:
            ans.append(S[i] + "(" + str(cnt[S[i]] - 1) + ")")
    print("\n".join(ans))
