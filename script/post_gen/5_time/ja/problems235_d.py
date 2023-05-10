Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, n = map(int, input().split())
    if a % 2 == 0:
        if n % 2 == 0:
            print(1)
        else:
            print(-1)
    else:
        print(-1)

=======
Suggestion 2

def solve():
    #a, n = map(int, input().split())
    a, n = 3, 72
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
        else:
            n -= 1
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 0:
        if n % a == 0:
            n //= a
            ans += 1
        elif n % a == 1:
            n -= 1
            ans += 1
        else:
            ans = -1
            break
    print(ans)

=======
Suggestion 4

def main():
    # 標準入力から a と N を取得する
    a, N = map(int, input().split())
    # 1 から N までの数について、操作を繰り返す回数を格納する配列を作成する
    dp = [-1] * (N + 1)
    # 1 から N までの数について、操作を繰り返す回数を求める
    for i in range(1, N + 1):
        # 操作を繰り返す回数を求める
        cnt = 0
        # 操作を繰り返す
        while i > 0:
            # 操作を繰り返す回数を増やす
            cnt += 1
            # i を a で割った余りを i に代入する
            i %= a
        # 操作を繰り返す回数を配列に格納する
        dp[i] = cnt
    # N について、操作を繰り返す回数を出力する
    print(dp[N])

=======
Suggestion 5

def main():
    a, n = map(int, input().split())
    cnt = 0
    while n > 1:
        if n % a == 0:
            n /= a
            cnt += 1
        elif n % 10 == 1:
            n -= 1
            n /= 10
            cnt += 1
        else:
            cnt = -1
            break
    print(cnt)

=======
Suggestion 6

def solve(a, n):
    if a == 1:
        return n - 1
    if a == n:
        return 1

    ans = 0
    while n > 0:
        if n % a == 0:
            n //= a
            ans += 1
        elif n % a != 1:
            return -1
        else:
            n -= 1
            ans += 1
    return ans

=======
Suggestion 7

def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 1:
        print(1)
        return
    if n % a == 0:
        count = 0
        while n > 1:
            n //= a
            count += 1
        print(count)
        return
    else:
        count = 0
        while n > 1:
            if n % a == 0:
                n //= a
                count += 1
            else:
                n = int(str(n)[-1] + str(n)[:-1])
                count += 1
        print(count)
        return

=======
Suggestion 8

def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n = n // a
            ans += 1
        elif n % 10 == 1:
            n = n // 10
            ans += 1
        else:
            ans = -1
            break
    print(ans)

=======
Suggestion 9

def main():
    a, n = map(int, input().split())
    if a == 1:
        print(n - 1)
        return
    x = 1
    for i in range(n):
        x *= a
        if x > n:
            print(i)
            return
    print(-1)

=======
Suggestion 10

def main():
    a, n = map(int, input().split())
    ans = 0
    while n != 1:
        if n % a != 0:
            n -= 1
            ans += 1
        elif n % a == 0:
            n /= a
            ans += 1
        if n == 0:
            print(-1)
            exit()
    print(ans)
