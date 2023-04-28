Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c)

=======
Suggestion 2

def main():
    s = input()
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    print(a+b+c)

=======
Suggestion 3

def main():
    abc = int(input())
    a = abc // 100
    b = abc // 10 % 10
    c = abc % 10
    print(a + b + c)

=======
Suggestion 4

def problem235_a():
    a = list(map(int, input()))
    print(a[0] + a[1] + a[2] + a[1] + a[2] + a[0] + a[2] + a[0] + a[1])

=======
Suggestion 5

def solve():
    # ここに書いてね
    abc = input()
    print(int(abc[0]) + int(abc[1]) + int(abc[2]))

=======
Suggestion 6

def main():
    n = input()
    print(int(n[0])+int(n[1])+int(n[2]))

=======
Suggestion 7

def solve():
    # 標準入力から abc を取得する
    abc = input()
    # abc を int 型に変換する
    abc = int(abc)
    # bca を計算する
    bca = abc // 100 + (abc // 10) % 10 * 100 + abc % 10 * 10
    # cab を計算する
    cab = abc % 10 * 100 + abc // 100 + (abc // 10) % 10 * 10
    # abc + bca + cab を計算する
    result = abc + bca + cab
    # 結果を出力する
    print(result)
