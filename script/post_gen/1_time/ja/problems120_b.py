Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    count = 0
    for i in range(min(A, B), 0, -1):
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                print(i)
                break

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    count = 0
    for i in range(max(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            count += 1
            if count == k:
                print(i)
                break

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    count = 0
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                print(i)
                break

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    count = 0
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            count += 1
        if count == K:
            print(i)
            break

=======
Suggestion 5

def main():
    A, B, K = map(int, input().split())
    cnt = 0
    for i in range(1, min(A, B)+1):
        if A % i == 0 and B % i == 0:
            cnt += 1
            if cnt == K:
                print(i)
                break

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    # A, B, K = 8, 12, 2
    # A, B, K = 100, 50, 4
    # A, B, K = 1, 1, 1
    # A, B, K = 100, 100, 100

    # A, B で割り切れる整数の個数
    c = 0
    # A, B で割り切れる整数の個数が K になった時の値
    ans = 0

    # A, B の最大公約数を求める
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # A, B の最小公倍数を求める
    def lcm(a, b):
        return a * b // gcd(a, b)

    # A, B の最小公倍数を求める
    L = lcm(A, B)

    # 1 から L までの間で、A, B で割り切れる整数の個数を求める
    for i in range(1, L + 1):
        if i % A == 0 and i % B == 0:
            c += 1
            ans = i

        if c == K:
            break

    print(ans)

=======
Suggestion 7

def main():
    A, B, K = map(int, input().split())
    divisor_list = []
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            divisor_list.append(i)
    print(divisor_list[-K])

=======
Suggestion 8

def main():
    A, B, K = map(int, input().split())
    ans = 0
    i = 0
    while True:
        if A % (A-i) == 0 and B % (A-i) == 0:
            ans = A-i
            K -= 1
        if K == 0:
            break
        i += 1
    print(ans)

=======
Suggestion 9

def main():
    A, B, K = map(int, input().split())
    # 1. A, Bの最大公約数を求める
    # 2. A, Bの最大公約数の約数を求める
    # 3. 2の約数を降順に並び替える
    # 4. K番目の約数を出力する

    # 1. A, Bの最大公約数を求める
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    c = gcd(A, B)

    # 2. A, Bの最大公約数の約数を求める
    d = []
    for i in range(1, c + 1):
        if c % i == 0:
            d.append(i)

    # 3. 2の約数を降順に並び替える
    d.sort(reverse=True)

    # 4. K番目の約数を出力する
    print(d[K - 1])

=======
Suggestion 10

def main():
    # 入力
    A, B, K = map(int, input().split())
    # リストを作成
    list = []
    # A,Bの最大公約数を求める
    for i in range(1, min(A, B)+1):
        if A % i == 0 and B % i == 0:
            list.append(i)
    # 出力
    print(list[-K])
