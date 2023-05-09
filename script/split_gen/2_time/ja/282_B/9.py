def main():
    #入力
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    #処理
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if 'o' in S[i]+S[j]:
                ans += 1
    #出力
    print(ans)
