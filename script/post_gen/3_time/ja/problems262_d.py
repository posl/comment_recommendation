Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(N):
        ans += pow(2, i, mod) * pow(2, N - 1 - i, mod) * A[i]
        ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += pow(2, i, 998244353) * (N - i) * A[i]
        ans %= 998244353
    print(ans)

main()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mod = 998244353
    ans = 0
    for i in range(n):
        ans += a[i] * pow(2, i, mod) * pow(2, n - i - 1, mod)
    print(ans % mod)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] == 0:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    
    ans = 0
    #Aの項を1個以上選ぶ方法は2^N-1通りある
    for i in range(1, 2**N):
        #選んだ項の平均値が整数であるものが何通りかを求める
        #平均値は、選んだ項の合計を選んだ項の個数で割る
        #選んだ項の合計は、選んだ項の2進数表現の1の個数を数えればわかる
        #選んだ項の個数は、選んだ項の2進数表現の1の個数を数えればわかる
        #選んだ項の2進数表現の1の個数を数える
        cnt = 0
        for j in range(N):
            if (i>>j) & 1:
                cnt += 1
        #選んだ項の合計を求める
        sum = 0
        for j in range(N):
            if (i>>j) & 1:
                sum += A[j]
        #選んだ項の合計を選んだ項の個数で割った余りが0になるものを数える
        if sum%cnt == 0:
            ans += 1
    print(ans%MOD)

=======
Suggestion 6

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #平均値が整数であるものの数をカウントする変数
    count = 0
    #A の項を選ぶ方法それぞれに対する平均値は以下のようになります。
    #平均値 = (a_1 + a_2 + ... + a_k) / k
    #k は選んだ項の数
    #k が 1 から N までの整数の時に平均値が整数であるかどうかを判定する
    for k in range(1, N + 1):
        #平均値が整数であるかどうかを判定する
        if sum(A[:k]) % k == 0:
            #平均値が整数である場合、カウントを 1 増やす
            count += 1
    #平均値が整数であるものの数を 998244353 で割った余りを出力
    print(count % 998244353)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(1,N+1):
        ans += (2**(N-i) - 2**(N-i-1)) * i * A[i-1]
        ans %= 998244353
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    # 1 から N までの整数の和を求める
    sum = 0
    for i in range(1, N+1):
        sum += i
    # 1 から N までの整数の和を N で割った余りを求める
    sum = sum % mod
    # 2^N-1 通りの選び方を求める
    ans = pow(2, N, mod) - 1
    # 2^N-1 通りの選び方を N で割った余りを求める
    ans = ans % mod
    # 2^N-1 通りの選び方を N で割った余りと 1 から N までの整数の和を N で割った余りを掛け合わせる
    ans = ans * sum
    # 2^N-1 通りの選び方を N で割った余りと 1 から N までの整数の和を N で割った余りを掛け合わせたものを N で割った余りを求める
    ans = ans % mod
    print(ans)
