def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == "0":
            cnt += 1
        else:
            if K > 0:
                K -= 1
                cnt += 1
            else:
                cnt -= 1
        ans = max(ans, cnt)
    print(ans)
