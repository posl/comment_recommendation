Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    l = len(s)
    ans = 0
    for i in range(l):
        for j in range(i+1, l+1):
            if int(s[i:j]) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    cnt = 0
    for i in range(N):
        for j in range(i+1,N+1):
            if int(S[i:j]) % 2019 == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    S = input()
    mod = 2019
    count = 0
    for i in range(len(S)):
        for j in range(i+1,len(S)+1):
            num = int(S[i:j])
            if num % mod == 0:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    s = input()
    mod = 2019
    l = len(s)
    ans = 0
    for i in range(l):
        for j in range(i+1,l+1):
            num = int(s[i:j])
            if num % mod == 0:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    S = S[::-1]
    ans = 0
    mod = 2019
    cnt = [0] * mod
    cnt[0] = 1
    d = 1
    now = 0
    for s in S:
        now += int(s) * d
        now %= mod
        d *= 10
        d %= mod
        ans += cnt[now]
        cnt[now] += 1
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    mod = 2019
    cnt = [0] * mod
    cnt[0] = 1
    a = 1
    s = 0
    for i in range(len(S)-1, -1, -1):
        s += int(S[i]) * a
        s %= mod
        cnt[s] += 1
        a *= 10
        a %= mod
    ans = 0
    for i in range(mod):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    S = S[::-1]
    mod = 2019
    count = 0
    num = 0
    for i in range(len(S)):
        num += int(S[i]) * pow(10, i, mod)
        num %= mod
        if num == 0:
            count += 1
    for i in range(1, len(S)):
        count += i * (int(S[i]) * pow(10, i-1, mod) % mod == 0)
    print(count)

=======
Suggestion 8

def main():
    S = input()
    mod = 2019
    # 各桁の数字を取り出してリストにする
    L = [int(s) for s in S]
    # 2019の倍数の個数
    ans = 0
    # 2019の倍数の個数を求める
    for i in range(len(L)):
        for j in range(i, len(L)):
            # i文字目からj文字目までの整数を求める
            num = 0
            for k in range(i, j+1):
                num = num * 10 + L[k]
            if num % mod == 0:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    S = input()
    N = len(S)
    #print(N)
    #print(S)
    #2019の倍数の最大値
    max = 2019 * 100000
    #print(max)
    #2019の倍数の最大値の桁数
    digit = len(str(max))
    #print(digit)
    #print(str(max))
    #print(str(max)[1:3])
    #print(str(max)[2:4])
    #print(str(max)[3:5])
    #print(str(max)[4:6])
    #print(str(max)[5:7])
    #print(str(max)[6:8])
    #print(str(max)[7:9])
    #print(str(max)[8:10])
    #print(str(max)[9:11])
    #print(str(max)[10:12])
    #print(str(max)[11:13])
    #print(str(max)[12:14])
    #print(str(max)[13:15])
    #print(str(max)[14:16])
    #print(str(max)[15:17])
    #print(str(max)[16:18])
    #print(str(max)[17:19])
    #print(str(max)[18:20])
    #print(str(max)[19:21])
    #print(str(max)[20:22])
    #print(str(max)[21:23])
    #print(str(max)[22:24])
    #print(str(max)[23:25])
    #print(str(max)[24:26])
    #print(str(max)[25:27])
    #print(str(max)[26:28])
    #print(str(max)[27:29])
    #print(str(max)[28:30])
    #print(str(max)[29:31])
    #print(str(max)[30:32])
    #print(str(max)[31:33])
    #print(str(max)[32:34])
    #print(str(max)[33:35])
    #print(str(max)[34:36])
    #print(str(max)[35:37])
    #print(str(max)[36:38])
    #print(str(max)[37:39])
    #print(str(max)[38:40])
    #print(str(max)[39:41])
    #print(str(max)[40:42])
    #print(str(max)[41:43])
    #

=======
Suggestion 10

def main():
    S = input()
    mod = 2019
    # 2019の倍数の文字列の長さは4以下なので、4桁を超えたらbreak
    # 0から9までの文字列の長さは200000以下なので、200000を超えたらbreak
    # 200000 * 4 = 800000
    # 800000 < 1000000
    # 0から9までの文字列の長さは1000000以下なので、1000000を超えたらbreak
    # 1000000 * 1 = 1000000
    # 1000000 < 2000000
    # 0から9までの文字列の長さは2000000以下なので、2000000を超えたらbreak
    # 2000000 * 1 = 2000000
    # 2000000 < 4000000
    # 0から9までの文字列の長さは4000000以下なので、4000000を超えたらbreak
    # 4000000 * 1 = 4000000
    # 4000000 < 8000000
    # 0から9までの文字列の長さは8000000以下なので、8000000を超えたらbreak
    # 8000000 * 1 = 8000000
    # 8000000 < 16000000
    # 0から9までの文字列の長さは16000000以下なので、16000000を超えたらbreak
    # 16000000 * 1 = 16000000
    # 16000000 < 32000000
    # 0から9までの文字列の長さは32000000以下なので、32000000を超えたらbreak
    # 32000000 * 1 = 32000000
    # 32000000 < 64000000
    # 0から9までの文字列の長さは64000000以下なので、64000000を超えたら
