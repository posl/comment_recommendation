def main():
    N = int(input())
    S = [input() for _ in range(N)]
    cnt = {}
    for i in range(N):
        if S[i] in cnt:
            cnt[S[i]] += 1
            S[i] += '(' + str(cnt[S[i]]) + ')'
        else:
            cnt[S[i]] = 0
    for i in range(N):
        print(S[i])
