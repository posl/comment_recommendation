Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    a, n = map(int, input().split())
    ans = 0
    while n != 1:
        if n % a == 0:
            n //= a
            ans += 1
        else:
            if len(str(n)) == 1:
                print(-1)
                return
            n = int(str(n)[-1] + str(n)[:-1])
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    a, n = map(int, input().split())
    count = 0
    while n > 1:
        if n % a == 0:
            n //= a
        elif n % 10 != 0:
            n = int(str(n % 10) + str(n // 10))
        else:
            break
        count += 1
    if n == 1:
        print(count)
    else:
        print(-1)

=======
Suggestion 3

def main():
    a, N = map(int, input().split())
    if N % a != 0:
        print(-1)
        return
    N //= a
    ans = 0
    while N > 0:
        if N % 10 == 1:
            N //= 10
        elif N % 2 == 0:
            N //= 2
        else:
            print(-1)
            return
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    a, n = map(int, input().split())
    x = 1
    ans = 0
    while x < n:
        ans += 1
        x = x * a
    print(ans)

=======
Suggestion 5

def main():
    #入力
    a, n = map(int, input().split())
    #初期値
    x = 1
    cnt = 0
    #処理
    while x < n:
        #a倍する
        x *= a
        cnt += 1
        #10で割り切れないなら
        if x % 10 != 0:
            #末尾の数字を先頭に持ってくる
            x = int(str(x)[-1] + str(x)[:-1])
            cnt += 1
    #出力
    if x == n:
        print(cnt)
    else:
        print(-1)

=======
Suggestion 6

def main():
    a, N = map(int, input().split())
    if N == a:
        print(1)
        return
    if N <= 1:
        print(-1)
        return
    if a == 2:
        print(len(bin(N)[2:]) - 1)
        return
    if a == 3:
        if N == 3:
            print(2)
        else:
            print(3)
        return
    if a == 4:
        if N == 4:
            print(2)
        else:
            print(3)
        return
    if a == 5:
        if N == 5:
            print(2)
        else:
            print(3)
        return
    if a == 6:
        if N == 6:
            print(2)
        else:
            print(3)
        return
    if a == 7:
        if N == 7:
            print(2)
        else:
            print(3)
        return
    if a == 8:
        if N == 8:
            print(2)
        else:
            print(3)
        return
    if a == 9:
        if N == 9:
            print(2)
        else:
            print(3)
        return
    if a == 10:
        if N == 10:
            print(2)
        else:
            print(3)
        return
    if a == 11:
        if N == 11:
            print(2)
        else:
            print(3)
        return
    if a == 12:
        if N == 12:
            print(2)
        else:
            print(3)
        return
    if a == 13:
        if N == 13:
            print(2)
        else:
            print(3)
        return
    if a == 14:
        if N == 14:
            print(2)
        else:
            print(3)
        return
    if a == 15:
        if N == 15:
            print(2)
        else:
            print(3)
        return
    if a == 16:
        if N == 16:
            print(2)
        else:
            print(3)
        return
    if a == 17:
        if N == 17:

=======
Suggestion 7

def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
    else:
        print(bfs(a, n))

=======
Suggestion 8

def solve(a, n):
    if n == 1:
        return 0
    elif n % a == 0:
        return solve(a, n // a) + 1
    else:
        num = n % 10
        if num == 1:
            return solve(a, n // 10) + 1
        elif num == 0:
            return -1
        else:
            return solve(a, n - num) + 1

=======
Suggestion 9

def main():
    a, N = map(int, input().split())
    if N % a == 0:
        print(-1)
        return

    # a が N の約数になるまでの回数
    count = 0
    while N % a != 0:
        N = int(str(N)[1:] + str(N)[0])
        count += 1
    print(count)
