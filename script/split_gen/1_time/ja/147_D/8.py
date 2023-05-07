def main():
    # 入力
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    # 処理
    ans = 0
    for i in range(60):
        cnt_1 = 0
        for a in A:
            if (a >> i) & 1:
                cnt_1 += 1
        ans += (2**i)*cnt_1*(N-cnt_1)
        ans %= mod
    # 出力
    print(ans)
