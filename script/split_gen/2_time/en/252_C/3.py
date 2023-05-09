def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(10):
        cnt = 0
        for j in range(N):
            if S[j][i] == str(i):
                cnt += 1
        ans += N - cnt
    print(ans)
