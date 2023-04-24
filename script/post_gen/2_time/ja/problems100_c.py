Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] // 2
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        while i % 2 == 0:
            count += 1
            i /= 2
    print(count)

=======
Suggestion 5

def main():
    # input
    n = int(input())
    a = list(map(int, input().split()))

    # compute
    cnt = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            cnt += 1

    # output
    print(cnt)

=======
Suggestion 6

def f(n):
    result = 0
    while n % 2 == 0:
        n = n / 2
        result += 1
    return result

n = int(input())
a = list(map(int, input().split()))

print(sum([f(a[i]) for i in range(n)]))

=======
Suggestion 7

def main():
    #input
    N = int(input())
    a = list(map(int, input().split()))

    #process
    cnt = 0
    for i in range(N):
        while True:
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
                cnt += 1
            else:
                break

    #output
    print(cnt)

=======
Suggestion 8

def main():
    # 標準入力から N と a を取得する
    N = int(input())
    a = list(map(int, input().split()))
    # 操作回数をカウントする変数
    count = 0
    # a の各要素に対して操作を行う
    for i in range(N):
        # a[i] が 2 で割り切れる間は 2 で割り続ける
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    # 操作回数を出力する
    print(count)

=======
Suggestion 9

def calc(a):
    if a%2 == 0:
        return calc(a/2) + 1
    else:
        return 0

=======
Suggestion 10

def main():
    # N:数列の長さ
    N = int(input())
    # a:数列
    a = list(map(int, input().split()))

    # 2で割り切れる回数をカウントする変数
    count = 0

    # 数列の各要素に対して、2で割り切れる回数をカウントする
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1

    print(count)
