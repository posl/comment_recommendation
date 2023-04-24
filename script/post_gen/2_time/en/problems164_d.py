Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        for j in range(i+1,N+1):
            if int(S[i:j]) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    if N <= 3:
        if int(S) % 2019 == 0:
            print(N * (N + 1) // 2)
        else:
            print(0)
        return
    S = list(map(int, S))
    S = [x * pow(10, i, 2019) for i, x in enumerate(S[::-1])]
    S = [sum(S[i:]) % 2019 for i in range(N)]
    ans = 0
    count = {}
    for s in S:
        if s in count:
            ans += count[s]
            count[s] += 1
        else:
            count[s] = 1
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    mod = 2019
    cnt = [0] * mod
    cnt[0] = 1
    ans = 0
    num = 0
    for i in range(n):
        num = (num + int(s[n - i - 1]) * pow(10, i, mod)) % mod
        cnt[num] += 1
    for i in range(mod):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    MOD = 2019
    ans = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            if int(S[i:j]) % MOD == 0:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    S = S[::-1]
    ans = 0
    d = [0] * 2019
    d[0] = 1
    num = 0
    for i in range(N):
        num += int(S[i]) * pow(10, i, 2019)
        num %= 2019
        ans += d[num]
        d[num] += 1
    print(ans)
    return

main()

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    R = 2019
    C = [0] * R
    C[0] = 1
    ans = 0
    d = 1
    for s in S[::-1]:
        ans += C[int(s) * d % R]
        C[int(s) * d % R] += 1
        d = d * 10 % R
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    M = 2019
    cnt = [0 for _ in range(M)]
    cnt[0] = 1
    ten = 1
    x = 0
    for i in range(N-1, -1, -1):
        x = (x + int(S[i]) * ten) % M
        ten = (ten * 10) % M
        cnt[x] += 1
    ans = 0
    for i in range(M):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    S = S[::-1]
    count = 0
    for i in range(4):
        if S[i] == '1':
            count += 1
    for i in range(4, len(S)):
        if S[i] == '1':
            count += 1
        if S[i] == '2':
            count += 1
    print(count)

=======
Suggestion 9

def main():
    S = input()
    #print(S)
    lenS = len(S)
    #print(lenS)
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print(S[64])
    #print(S[65])
    #print(S[66])
    #print(S[67

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    s = s[::-1]
    ans = 0
    mod = 2019
    #print(s)
    #print(n)
    d = [0] * mod
    d[0] = 1
    now = 0
    for i in range(n):
        now += int(s[i]) * pow(10, i, mod)
        now %= mod
        ans += d[now]
        d[now] += 1
    print(ans)
