Synthesizing 9/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

for i in range(c, d+1):
    if is_prime(a + i):
        print('Takahashi')
        exit()

for i in range(a, b+1):
    if not is_prime(i + d):
        print('Aoki')
        exit()

print('Takahashi')

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

A, B, C, D = map(int, input().split())
takahashi = 0
aoki = 0
for i in range(A, B + 1):
    for j in range(C, D + 1):
        if is_prime(i + j):
            aoki += 1
        else:
            takahashi += 1

=======
Suggestion 3

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

A, B, C, D = map(int, input().split())
for i in range(A, B+1):
    for j in range(C, D+1):
        if is_prime(i+j):
            print("Aoki")
            exit()
print("Takahashi")

=======
Suggestion 5

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i+j):
            print('Aoki')
            exit()

print('Takahashi')

=======
Suggestion 6

def prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

A,B,C,D = map(int,input().split())
for i in range(A,B+1):
    for j in range(C,D+1):
        if prime(i+j):
            print("Aoki")
            exit()
print("Takahashi")

=======
Suggestion 7

def prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())
for i in range(a, b + 1):
    for j in range(c, d + 1):
        if prime(i + j):
            print("Aoki")
            exit()
print("Takahashi")

問題文
高橋君と青木君が次のようなゲームをします。

まず、高橋君が A 以上 B 以下の好きな整数を選び、青木君に伝える
次に、青木君が C 以上 D 以下の好きな整数を選ぶ
二人の選んだ整数の和が素数なら青木君の勝ち、そうでなければ高橋君の勝ち
二人が最適な戦略を取るとき、どちらが勝ちますか？

制約
1 ≦ A ≦ B ≦ 100
1 ≦ C ≦ D ≦ 100
入力に含まれる値は全て整数である

入力
入力は以下の形式で標準入力から与えられる。
A B C D

出力
二人が最適な戦略をとったとき、高橋君が勝つなら Takahashi、青木君が勝つなら Aoki を出力せよ。

入力例 1
2 3 3 4

出力例 1
Aoki
例えば高橋君が 2 を選んだときは、青木君は 3 を選ぶことで、和を素数であ

=======
Suggestion 8

def main():
    A,B,C,D = map(int,input().split())
    if B < C or D < A:
        print("Aoki")
    else:
        print("Takahashi")

=======
Suggestion 9

def main():
    A, B, C, D = map(int, input().split())
    prime = [0] * 1000
    for i in range(3, 1000, 2):
        prime[i] = 1
    for i in range(3, 1000, 2):
        if prime[i]:
            for j in range(i * 2, 1000, i):
                prime[j] = 0
    for i in range(A, B + 1):
        for j in range(C, D + 1):
            if prime[i + j] == 1:
                print("Aoki")
                return
    print("Takahashi")
