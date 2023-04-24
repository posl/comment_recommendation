Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    count = 0
    for i in range(1,K+1):
        if i%2 == 0:
            for j in range(1,K+1):
                if j%2 == 1:
                    count += 1
    print(count)

=======
Suggestion 2

def main():
    K = int(input())
    ans = 0
    for i in range(1, K+1):
        if i % 2 == 0:
            ans += (K - i) // 2
        else:
            ans += (K - i + 1) // 2
    print(ans)

=======
Suggestion 3

def main():
    K = int(input())
    even = K // 2
    odd = K - even
    print(even * odd)

=======
Suggestion 4

def main():
    # 入力
    K = int(input())
    # 処理
    even = K//2
    odd = K//2 + K%2
    # 出力
    print(even*odd)

=======
Suggestion 5

def main():
    #入力
    K = int(input())
    #偶数の数
    even = K//2
    #奇数の数
    odd = K - even
    #出力
    print(even * odd)

=======
Suggestion 6

def main():
    k = int(input())
    print(k*(k-1)//2)

=======
Suggestion 7

def main():
    K = int(input())
    print(K*(K-1)//2)

=======
Suggestion 8

def main():
    k = int(input())
    k = k // 2
    print(k * (k + 1))

=======
Suggestion 9

def main():
    # 入力
    k = int(input())
    # 処理
    if k%2==0:
        k = k//2
        print(k*(k-1))
    else:
        k = k//2
        print(k*(k+1))

=======
Suggestion 10

def main():
    #標準入力からKを取得
    K = int(input())
    #Kが2以上100以下の場合
    if 2 <= K and K <= 100:
        #偶数の数を格納する変数を定義
        even = 0
        #奇数の数を格納する変数を定義
        odd = 0
        #1からKまでの数を順に取得
        for i in range(1,K+1):
            #iが偶数の場合
            if i % 2 == 0:
                #偶数の数を1増やす
                even += 1
            #iが奇数の場合
            else:
                #奇数の数を1増やす
                odd += 1
        #偶数の数と奇数の数を掛け合わせた数を出力
        print(even * odd)
