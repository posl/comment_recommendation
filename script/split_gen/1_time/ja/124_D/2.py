def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == '0':
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(min(N-1, ans+2*K))
