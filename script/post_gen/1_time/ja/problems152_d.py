Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = [0] * 10
    b = [0] * 10
    for i in range(1, N + 1):
        a[i % 10] += 1
        b[i // 10 % 10] += 1
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += a[i] * b[j] * (i == j)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if i < 10:
            count += 1
        else:
            if str(i)[0] == str(i)[-1]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    #N以下の整数の組(A,B)で、Aの末尾の桁がBの先頭の桁に等しく、Aの先頭の桁がBの末尾の桁に等しい
    #A,Bを先頭に0のつかない10進数表記で表したときに、
    #Aの末尾の桁がBの先頭の桁に等しく、Aの先頭の桁がBの末尾の桁に等しい
    #Aの末尾の桁はBの先頭の桁に等しく、Aの先頭の桁はBの末尾の桁に等しい
    #Aの先頭の桁はBの末尾の桁に等しい
    #Aの末尾の桁はBの先頭の桁に等しい
    #Aの先頭の桁はBの末尾の桁に等しい
    #Aの末尾の桁はBの先頭の桁に等しい
    #Aの先頭の桁はBの末尾の桁に等しい
    #Aの末尾の桁はBの先頭の桁に等しい
    #Aの先頭の桁はBの末尾の桁に等しい
    #Aの末尾の桁はBの先頭の桁に等しい
    #Aの先頭の桁はBの末尾の桁に等しい
    #Aの末尾の桁はBの先頭の桁に等しい
    #Aの先頭の桁はBの末尾の桁に等しい
    #Aの末尾の桁はBの先頭の桁に等しい
    #Aの先

=======
Suggestion 4

def main():
    # 入力
    N = int(input())
    # 処理
    ans = 0
    for i in range(1,N+1):
        for j in range(i,N+1):
            if i%10==j//10%10 and i//10%10==j%10:
                ans += 1
    # 出力
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    if N < 10:
        print(N)
        return
    else:
        ans = 9
        for i in range(10,N+1):
            if str(i)[0] == str(i)[len(str(i))-1]:
                ans += 1
        print(ans)

main()

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    #桁数を求める
    digit = 0
    while 10**digit <= N:
        digit += 1
    #print(digit)
    #各桁の数を求める
    digit_num = [0]*digit
    for i in range(digit):
        digit_num[i] = (N//10**(i+1))*10**i + max(0, N%10**i+1-10**i)
    #print(digit_num)
    #各桁の数の総和を求める
    digit_total = [0]*digit
    for i in range(digit):
        if i == 0:
            digit_total[i] = digit_num[i]
        else:
            digit_total[i] = digit_total[i-1] + digit_num[i]
    #print(digit_total)
    #答えを求める
    for i in range(digit):
        if i == 0:
            ans += digit_total[i]
        else:
            ans += digit_total[i]*2
    print(ans)

=======
Suggestion 7

def main():
    #入力
    N = int(input())
    
    #初期化
    ans = 0
    cnt = [0]*10
    cnt2 = [0]*10
    for i in range(1,N+1):
        cnt[i%10] += 1
        cnt2[i//10] += 1
    for i in range(10):
        ans += cnt[i] * cnt2[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())

    # 10 進数表記で表したときの桁数を求める
    def digit(n):
        if n == 0:
            return 1
        else:
            return len(str(n))

    # 10 進数表記で表したときの先頭の桁を求める
    def head(n):
        return int(str(n)[0])

    # 10 進数表記で表したときの末尾の桁を求める
    def tail(n):
        return int(str(n)[-1])

    # 10 進数表記で表したときの先頭の桁と末尾の桁が等しいか否かを判定する
    def head_tail(n):
        return head(n) == tail(n)

    # 10 進数表記で表したときの末尾の桁と先頭の桁が等しいか否かを判定する
    def tail_head(n):
        return tail(n) == head(n)

    # 10 進数表記で表したときの先頭の桁と末尾の桁が等しいものの個数を求める
    def head_tail_count(n):
        count = 0
        for i in range(1, n+1):
            if head_tail(i):
                count += 1
        return count

    # 10 進数表記で表したときの末尾の桁と先頭の桁が等しいものの個数を求める
    def tail_head_count(n):
        count = 0
        for i in range(1, n+1):
            if tail_head(i):
                count += 1
        return count

    # 10 進数表記で表したときの先頭の桁と末尾の桁が等しいものの個数を求める
    def head_tail_count2(n):
        count = 0
        for i in range(1, n+1):
            if

=======
Suggestion 9

def main():
    n = int(input())
    # 1桁の数値は条件を満たさないので2桁以降のみ考える
    # 1桁の数値の組み合わせを数える
    # 10^5までの数値の組み合わせを数える
    # 2桁の数値の組み合わせを数える
    # 10^5までの数値の組み合わせを数える
    # 3桁の数値の組み合わせを数える
    # 10^5までの数値の組み合わせを数える
    # 4桁の数値の組み合わせを数える
    # 10^5までの数値の組み合わせを数える
    # 5桁の数値の組み合わせを数える
    # 10^5までの数値の組み合わせを数える
    # 6桁の数値の組み合わせを数える
    # 10^5までの数値の組み合わせを数える
    # 7桁の数値の組み合わせを数える
    # 10^5までの数値の組み合わせを数える
    # 8桁の数値の組み合わせを数える
    # 10^5までの数値の組み合わせを数える
    # 9桁の数値の組み合わせを数える
    # 10^5までの数値の組み合わせを数える
    # 10桁の数値の組み合わせを数える
    # 10^5までの数値の組み合わせを数える
