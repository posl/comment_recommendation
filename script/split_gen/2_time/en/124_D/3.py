def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "0":
            ans += 1
            for j in range(i+1, N):
                if S[j] == "1":
                    ans += 1
                else:
                    break
            break
    for i in range(N-1, -1, -1):
        if S[i] == "0":
            ans += 1
            for j in range(i-1, -1, -1):
                if S[j] == "1":
                    ans += 1
                else:
                    break
            break
    cnt = 0
    for i in range(N):
        if S[i] == "1":
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(min(ans+2*K, N))
