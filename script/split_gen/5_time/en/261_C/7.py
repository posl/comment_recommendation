def main():
    N = int(input())
    S = [input() for i in range(N)]
    cnt = {}
    for i in range(N):
        if S[i] not in cnt:
            cnt[S[i]] = 0
        cnt[S[i]] += 1
        if cnt[S[i]] == 1:
            print(S[i])
        else:
            print(S[i] + '(' + str(cnt[S[i]]-1) + ')')
