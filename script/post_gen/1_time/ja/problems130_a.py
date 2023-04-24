Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X, A = map(int, input().split())
    if X < A:
        print(0)
    else:
        print(10)

=======
Suggestion 2

def main():
    X, A = map(int, input().split())
    if X < A:
        print(0)
    else:
        print(10)
main()

=======
Suggestion 3

def main():
    # X, A は 0 以上 9 以下の整数です。
    # X が A 未満の時 0、A 以上の時 10 を出力してください。
    # X, A = map(int, input().split())
    X, A = map(int, input().split())
    if X < A:
        print(0)
    else:
        print(10)

=======
Suggestion 4

def main():
    #入力
    X, A = map(int, input().split())

    #出力
    if X < A:
        print(0)
    else:
        print(10)
