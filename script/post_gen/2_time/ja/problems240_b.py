Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(len(set(A)))

=======
Suggestion 4

def main():
    N = int(input())
    a = [int(x) for x in input().split()]
    print(len(set(a)))

=======
Suggestion 5

def main():
    #入力
    N = int(input())
    a = list(map(int, input().split()))

    #処理
    ans = len(set(a))

    #出力
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = 0
    for i in range(N):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    # 標準入力から1行読み込み、整数に変換し、変数nに代入する
    n = int(input())
    # 標準入力から1行読み込み、スペース区切りでリストに変換し、変数aに代入する
    a = list(map(int, input().split()))
    # 重複を排除したリストをset_aに代入する
    set_a = set(a)
    # set_aの要素数を出力する
    print(len(set_a))
