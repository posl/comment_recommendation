def main():
    S = input()
    Q = S.count('?')
    mod = 10**9+7
    ans = 0
    for i in range(3**Q):
        tmp = ''
        for j in range(Q):
            if i%(3**(j+1))//(3**j) == 0:
                tmp += 'A'
            elif i%(3**(j+1))//(3**j) == 1:
                tmp += 'B'
            else:
                tmp += 'C'
        tmp = tmp[::-1]
        cnt = 0
        for j in range(len(S)):
            if S[j] == '?':
                S = S[:j] + tmp[cnt] + S[j+1:]
                cnt += 1
        cnt = 0
        for j in range(len(S)-2):
            if S[j] == 'A' and S[j+1] == 'B' and S[j+2] == 'C':
                cnt += 1
        ans += cnt
    print(ans%mod)
