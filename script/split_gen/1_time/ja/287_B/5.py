def main():
    #入力
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    #処理
    ans = 0
    for s in S:
        ans += sum([s[-3:] == t for t in T])
    #出力
    print(ans)
