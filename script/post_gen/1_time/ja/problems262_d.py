Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, N+1):
        ans += pow(2, i-1, MOD) * pow(2, N-i, MOD) * i * A[i-1]
        ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    mod = 998244353
    ans = 0
    for i in range(N):
        ans += (pow(2, i, mod) - pow(2, N-i-1, mod)) * A[i]
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, N+1):
        ans += (A[i-1]*pow(2, N-i, MOD))%MOD
        ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353

    # 1個以上選ぶ方法は 2^N-1 通り
    # そのうち選んだ項の平均値が整数であるものが何通りかを 998244353 で割った余りを求めてください。
    # 1個以上選ぶ方法は 2^N-1 通り
    # そのうち選んだ項の平均値が整数であるものが何通りかを 998244353 で割った余りを求めてください。
    # 1個以上選ぶ方法は 2^N-1 通り
    # そのうち選んだ項の平均値が整数であるものが何通りかを 998244353 で割った余りを求めてください。
    # 1個以上選ぶ方法は 2^N-1 通り
    # そのうち選んだ項の平均値が整数であるものが何通りかを 998244353 で割った余りを求めてください。
    # 1個以上選ぶ方法は 2^N-1 通り
    # そのうち選んだ項の平均値が整数であるものが何通りかを 998244353 で割った余りを求めてください。
    # 1個以上選ぶ方法は 2^N-1 通り
    # そのうち選んだ項の平均値が整数であるものが何通りかを 998244353 で割った余りを求めてください。
    # 1個以上選ぶ方法は 2^N-1 通り
    # そのうち選んだ項

=======
Suggestion 5

def main():
    # 1行目の入力
    N = int(input())
    # 2行目の入力
    A = list(map(int, input().split()))
    # 結果の出力
    print(sum(A) * (2 ** (N - 1)) % 998244353)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # 2^N-1 通りの選び方
    # 2^N-1 通りの選び方のうち、整数の平均値を持つものが何通りかを求める
    # 2^N-1 通りの選び方は、選ばない場合と選ぶ場合の2通り
    # 選ばない場合は、選ぶ場合の数に含まれているので、
    # 選ぶ場合の数を求める
    # 選ぶ場合の数は、2^(N-1) 通り
    # 2^(N-1) 通りの選び方のうち、整数の平均値を持つものが何通りかを求める
    # 2^(N-1) 通りの選び方は、選ばない場合と選ぶ場合の2通り
    # 選ばない場合は、選ぶ場合の数に含まれているので、
    # 選ぶ場合の数を求める
    # 選ぶ場合の数は、2^(N-2) 通り
    # 2^(N-2) 通りの選び方のうち、整数の平均値を持つものが何通りかを求める
    # 2^(N-2) 通りの選び方は、選ばない場合と選ぶ場合の2通り
    # 選ばない場合は、選ぶ場合の数に含まれているので、
    # 選ぶ場合の数を求める
    # 選ぶ場合の数は、2^(N-3

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])
    #print(A[63])
    #print(A[64])
    #print(A[65])
    #print

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    #print(N, A)
    #print(MOD)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    sum = sum * pow(2, MOD - 2, MOD)
    sum = sum % MOD
    #print(sum)
    ans = sum * pow(2, N - 1, MOD)
    ans = ans % MOD
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353

    #nCkを求める関数
    def combination(n,k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        a = 1
        b = 1
        for i in range(k):
            a = a * (n - i) % mod
            b = b * (i + 1) % mod
        return a * pow(b,mod-2,mod) % mod

    #Aの項を選ぶ方法それぞれに対する平均値が整数となるものの通り数を求める
    ans = 0
    for i in range(N):
        #Aのi番目の項を選ぶ場合
        ans += combination(N-1,i) * A[i]
        ans %= mod
    print(ans)
