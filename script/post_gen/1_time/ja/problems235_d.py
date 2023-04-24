Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, n = map(int, input().split())
    count = 0
    while n != 1:
        if n % a == 0:
            n = n // a
            count += 1
        elif n % 10 == 0:
            n = n // 10
            count += 1
        else:
            n = (n % 10) * (10 ** (len(str(n)) - 1)) + (n // 10)
            count += 1
    print(count)

=======
Suggestion 2

def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
        elif n % 10 == 1:
            n //= 10
        else:
            print(-1)
            return
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
        elif n % 10 != 0:
            n = int(str(n % 10) + str(n // 10))
        else:
            ans = -1
            break
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    a, N = map(int, input().split())
    ans = 0
    while N > 1:
        if N % a == 0:
            N //= a
        else:
            if N % 10 == 0:
                N //= 10
            else:
                print(-1)
                return
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    a, n = map(int, input().split())
    if a == 10:
        if n == 10:
            print(1)
        else:
            print(-1)
        return
    if n == a:
        print(2)
        return
    if n < a:
        print(-1)
        return
    ans = 0
    while n > 0:
        if n % a == 0:
            n //= a
            ans += 1
        else:
            n -= 1
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    a, n = map(int, input().split())
    if a == n:
        print(0)
        return
    elif a > n:
        print(-1)
        return
    else:
        pass

    # 一桁目を取り出す
    def get_first_digit(num):
        while num >= 10:
            num //= 10
        return num

    # 一桁目を取り出す
    def get_last_digit(num):
        return num % 10

    # 一桁目を取り出す
    def get_first_digit(num):
        while num >= 10:
            num //= 10
        return num

    # 一桁目を取り出す
    def get_last_digit(num):
        return num % 10

    # 一桁目を取り出す
    def get_first_digit(num):
        while num >= 10:
            num //= 10
        return num

    # 一桁目を取り出す
    def get_last_digit(num):
        return num % 10

    # 一桁目を取り出す
    def get_first_digit(num):
        while num >= 10:
            num //= 10
        return num

    # 一桁目を取り出す
    def get_last_digit(num):
        return num % 10

    # 一桁目を取り出す
    def get_first_digit(num):
        while num >= 10:
            num //= 10
        return num

    # 一桁目を取り出す
    def get_last_digit(num):
        return num % 10

    # 一桁目を取り出す
    def get_first_digit(num):
        while num >= 10:
            num //= 10
        return num

    # 一桁目を取り出す
    def get_last_digit(num):
        return num % 10

    # 一桁目を取り出す
    def get_first_digit(num):
        while num >= 10:
            num //= 10
        return num

    # 一桁目を取り出す
    def get_last_digit(num):
        return num % 10

    # 一

=======
Suggestion 7

def main():
    a, n = map(int, input().split())
    if n % a != 0:
        print(-1)
        return
    x = n // a
    if x == 1:
        print(1)
        return
    if x % 2 == 0:
        print(2)
        return
    if x % 2 == 1:
        print(3)
        return

=======
Suggestion 8

def main():
    a, n = list(map(int, input().split()))
    q = [1]
    v = [0] * (n + 1)
    v[1] = 1
    while q:
        x = q.pop(0)
        if x == n:
            print(v[x] - 1)
            return
        if x * a <= n and v[x * a] == 0:
            q.append(x * a)
            v[x * a] = v[x] + 1
        if x % 10 != 0 and v[x * 10 + x % 10] == 0:
            q.append(x * 10 + x % 10)
            v[x * 10 + x % 10] = v[x] + 1
    print(-1)

=======
Suggestion 9

def main():
    a, n = map(int, input().split())

    # 1桁の時の計算
    if n < 10:
        if n == 1:
            print(0)
        elif n % a == 0:
            print(1)
        else:
            print(-1)
        return

    # 2桁以上の時の計算
    # 2桁目以降の計算
    ans = 1
    while True:
        ans += 1
        n = int(str(n)[-1] + str(n * a)[-1])
        if n % a != 0:
            print(-1)
            return
        if n == 10:
            n = 1
        if n == 1:
            break
    print(ans)

=======
Suggestion 10

def main():
    a, N = map(int, input().split())
    # 1回目の操作で変化できる数値のリスト
    # 2回目の操作で変化できる数値のリスト
    # 3回目の操作で変化できる数値のリスト
    # ...
    # という風に、操作回数をインデックスに持つリストを作成
    # 例: a = 2, N = 767090 の場合
    # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472, 274877906944, 549755813888, 1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416, 35184372088832, 70368744177664, 140737488355328, 281474976710656, 562949953421312, 1125899906842624, 2251799813685248, 4503599627370496, 9007199254740992, 18014398509481984, 36028797018963968, 72057594037927936, 144115188075855872, 288230376151711744, 576460752303423488, 1152921504606846976, 2305843009213693952, 4611686018427387904, 9223372036854775808, 184467440
