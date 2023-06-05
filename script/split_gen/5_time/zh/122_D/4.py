def main():
    N = int(input())
    mod = 10**9+7
    dp = [0] * (4**3)
    #dp[i] := 末尾3文字がAGCでない文字列の個数
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                #AGCでない文字列でない場合
                if (c2 == 0 and c3 == 2) or (c2 == 2 and c3 == 0) or (c1 == 0 and c3 == 2):
                    continue
                dp[c1*16+c2*4+c3] = 1
    for i in range(4**3):
        #末尾につける文字
        c1 = i // 16
        #末尾から2番目につける文字
        c2 = (i//4) % 4
        #末尾から3番目につける文字
        c3 = i % 4
        for a in range(4):
            #追加する文字
            if (c2 == 0 and c3 == 2) or (c2 == 2 and c3 == 0) or (c1 == 0 and c3 == 2):
                continue
            if (a == 0 and c2 == 2 and c3 == 1) or (a == 0 and c2 == 1 and c3 == 2):
                continue
            dp[a*16+c1*4+c2] += dp[i]
            dp[a*16+c1*4+c2] %= mod
    ans = 0
    for i in range(4**3):
        ans += dp[i]
        ans %= mod
    print(ans)
