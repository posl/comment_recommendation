Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        for j in range(i+3,len(S)+1):
            if int(S[i:j]) % 2019 == 0:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    ans = 0
    cnt = [0] * 2019
    cnt[0] = 1
    d = 1
    for i in range(n - 1, -1, -1):
        ans += cnt[d * int(s[i]) % 2019]
        cnt[d * int(s[i]) % 2019] += 1
        d = d * 10 % 2019
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i+3,n):
            if int(s[i:j+1]) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 4

def solve():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if int(s[i:j+1]) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    s_len = len(s)
    count = 0
    for i in range(s_len):
        for j in range(i+3, s_len+1):
            if int(s[i:j]) % 2019 == 0:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    a = [0] * n
    a[-1] = int(s[-1])
    for i in range(n-2, -1, -1):
        a[i] = (int(s[i]) * pow(10, n-i-1) + a[i+1]) % 2019
    b = [0] * 2019
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(2019):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(0, N-3):
        for j in range(i+3, N):
            if int(S[i:j+1])%2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    #print(s)
    #print(len(s))
    #print(type(s))
    #print(s[0])
    #print(s[1])
    #print(s[2])
    #print(s[3])
    #print(s[4])
    #print(s[5])
    #print(s[6])
    #print(s[7])
    #print(s[8])
    #print(s[9])
    #print(s[10])
    #print(s[11])
    #print(s[12])
    #print(s[13])
    #print(s[14])
    #print(s[15])
    #print(s[16])
    #print(s[17])
    #print(s[18])
    #print(s[19])
    #print(s[20])
    #print(s[21])
    #print(s[22])
    #print(s[23])
    #print(s[24])
    #print(s[25])
    #print(s[26])
    #print(s[27])
    #print(s[28])
    #print(s[29])
    #print(s[30])
    #print(s[31])
    #print(s[32])
    #print(s[33])
    #print(s[34])
    #print(s[35])
    #print(s[36])
    #print(s[37])
    #print(s[38])
    #print(s[39])
    #print(s[40])
    #print(s[41])
    #print(s[42])
    #print(s[43])
    #print(s[44])
    #print(s[45])
    #print(s[46])
    #print(s[47])
    #print(s[48])
    #print(s[49])
    #print(s[50])
    #print(s[51])
    #print(s[52])
    #print(s[53])
    #print(s[54])
    #print(s[55])
    #print(s[56])
    #print(s[57])
    #print(s[58])
    #print(s[59])
    #print(s[60])
    #print(s[61])
    #print(s[62])
    #print(s[63])
    #print(s[64])
    #print(s[65])
    #print(s[66])
    #print(s[67])

=======
Suggestion 9

def solve(S):
    # 2019の倍数の条件は、
    # 1. 2019の倍数の数の桁数は2019の倍数
    # 2. 2019の倍数の数は、2019で割った余りが0
    # 3. 2019の倍数の数は、2019で割った余りが2019-1
    # 4. 2019の倍数の数は、2019で割った余りが2019-2
    # 5. 2019の倍数の数は、2019で割った余りが2019-3
    # 6. 2019の倍数の数は、2019で割った余りが2019-4
    # 7. 2019の倍数の数は、2019で割った余りが2019-5
    # 8. 2019の倍数の数は、2019で割った余りが2019-6
    # 9. 2019の倍数の数は、2019で割った余りが2019-7
    # 10. 2019の倍数の数は、2019で割った余りが2019-8
    # 11. 2019の倍数の数は、2019で割った余りが2019-9
    # という条件を満たす
    # つまり、2019の倍数の数は、2019で割った余りが0-9の数の和になる
    # 余りが0の数の個数を数える
    # 余りが1の数の個数を数える
    # 余りが2の数の個数を数える
    # 余りが3の数の個数を数える
    # 余りが4の数の個数を数える
    # 余りが5の数の個数を数える
    # 余りが
