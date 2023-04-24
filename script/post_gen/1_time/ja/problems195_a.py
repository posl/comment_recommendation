Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    M, H = map(int, input().split())
    if H % M == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    m, h = map(int, input().split())
    if h % m == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    m, h = map(int, input().split())
    if h % m == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    m, h = map(int, input().split())
    print('Yes' if h % m == 0 else 'No')

=======
Suggestion 5

def main():
    #入力
    M, H = map(int, input().split())
    #出力
    print("Yes" if H % M == 0 else "No")

=======
Suggestion 6

def main():
    # 標準入力から1行取得
    # 1行目の入力値をスペースで分割して、リストに変換
    # map()関数で、リストの各要素をint型に変換
    m, h = map(int, input().split())
    # hをmで割った余りが0ならYes、そうでなければNoを出力
    print("Yes" if h % m == 0 else "No")
