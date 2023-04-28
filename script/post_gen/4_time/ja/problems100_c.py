Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
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
            a[i] = a[i] / 2
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    # N = int(input())
    # a = list(map(int, input().split()))

    N = 10
    a = [2184, 2126, 1721, 1800, 1024, 2528, 3360, 1945, 1280, 1776]

    cnt = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] // 2
            cnt += 1

    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0

    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            ans += 1

    print(ans)

=======
Suggestion 6

def main():
    # 標準入力受付
    n = int(input())
    a = list(map(int, input().split()))
    # 処理
    count = 0
    for i in range(n):
        num = a[i]
        while num % 2 == 0:
            count += 1
            num = num / 2
    # 標準出力
    print(count)

=======
Suggestion 7

def count_div2(x):
    count = 0
    while x%2 == 0:
        x = x/2
        count += 1
    return count

n = int(input())
a = list(map(int,input().split()))

count = 0
for i in range(n):
    count += count_div2(a[i])

print(count)

=======
Suggestion 8

def count_divide_2(n):
    count = 0
    while n % 2 == 0:
        n = n / 2
        count += 1
    return count

=======
Suggestion 9

def div2or3(n):
    if n % 3 == 0:
        return n / 3
    elif n % 2 == 0:
        return n / 2
    else:
        return False

=======
Suggestion 10

def main():
    # Nを取得する
    N = int(input())
    # aを取得する
    a = list(map(int, input().split()))
    # print(N)
    # print(a)

    # 操作回数をカウントする変数を定義する
    count = 0

    # aの要素を順番に操作する
    for i in range(N):
        # aの要素が奇数の場合は終了する
        if a[i] % 2 != 0:
            continue
        # aの要素が偶数の場合は操作する
        else:
            # 操作回数をカウントする
            count += 1
            # aの要素を2で割る
            a[i] = a[i] / 2
            # aの要素が偶数になるまで操作する
            while a[i] % 2 == 0:
                # 操作回数をカウントする
                count += 1
                # aの要素を2で割る
                a[i] = a[i] / 2

    # 結果を出力する
    print(count)
