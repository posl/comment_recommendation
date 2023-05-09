def main():
    S = input()
    n = len(S)
    MOD = 10**9+7
    ans = 0
    cnt = 0
    for i in range(n):
        if S[i] == 'A':
            ans += pow(3,cnt,MOD)
        elif S[i] == '?':
            ans += pow(3,cnt+1,MOD)
            cnt += 1
    print(ans%MOD)
