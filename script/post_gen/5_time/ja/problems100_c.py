Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] //= 2
            cnt += 1
    print(cnt)

=======
Suggestion 2

def check(n):
    if n % 2 == 0:
        return 1 + check(n/2)
    else:
        return 0

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    ans += check(i)

print(ans)

=======
Suggestion 3

def cal(a):
    count = 0
    for i in range(len(a)):
        while a[i]%2 == 0:
            a[i] = a[i] / 2
            count += 1
    return count

n = int(input())
a = list(map(int, input().split()))
print(cal(a))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            cnt += 1
    print(cnt)

=======
Suggestion 5

def count_2(n):
    if n%2 != 0:
        return 0
    else:
        return 1 + count_2(n/2)

n = int(input())
a = list(map(int, input().split()))
print(sum([count_2(i) for i in a]))

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    print(count)

=======
Suggestion 7

def main():
    # 標準入力受け取り
    n = int(input())
    a = list(map(int, input().split()))
    # 最大操作回数
    cnt = 0
    # 2で割れる回数
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            cnt += 1
    # 出力
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while(a[i] % 2 == 0):
            a[i] = a[i] // 2
            count += 1
    print(count)

=======
Suggestion 9

def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input()
    # input_lineをスペースで区切ってinput_line_splitに入れる
    input_line_split = input_line.split()
    # input_line_splitの要素をintに変換してinput_line_intに入れる
    input_line_int = [int(i) for i in input_line_split]
    # Nを取得
    N = input_line_int[0]
    # aを取得
    a = input_line_int[1:]
    # 操作回数
    count = 0
    # aの要素を順番に操作し、全ての要素が偶数になるまで操作を繰り返す
    while all(i % 2 == 0 for i in a):
        a = [i / 2 for i in a]
        count += 1
    # 操作回数を出力
    print(count)

=======
Suggestion 10

def count_div2(num):
    count = 0
    while num % 2 == 0:
        count += 1
        num /= 2
    return count
