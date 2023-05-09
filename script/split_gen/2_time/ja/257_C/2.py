def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[j] == "0" and W[j] < W[i]:
                cnt += 1
            if S[j] == "1" and W[j] >= W[i]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
