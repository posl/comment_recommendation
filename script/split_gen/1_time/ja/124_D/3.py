def main():
    N, K = map(int, input().split())
    S = input()
    cnt = 0
    ans = 0
    for i in range(N):
        if S[i] == '0':
            cnt += 1
            if cnt == K + 1:
                ans += 1
                cnt -= 1
        else:
            ans += cnt
            cnt = 0
    ans += cnt
    print(ans)
