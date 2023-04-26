Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(B // A)
    else:
        print(B // A + 1)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(b // a)
    else:
        print(b // a + 1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print((b + a - 3) // (a - 1))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print((B + A - 1) // A)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print((B+A-3)//(A-1))

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print((B-1+A-2)//(A-1))

=======
Suggestion 7

def main():
    A,B = map(int, input().split())
    if B <= A:
        print(1)
    else:
        if (B-A) % (A-1) == 0:
            print((B-A)//(A-1)+1)
        else:
            print((B-A)//(A-1)+2)

=======
Suggestion 8

def main():
    # A:電源タップのポート数, B:未使用の差込口数
    A, B = map(int, input().split())
    # 電源タップの個数
    cnt = 1
    # 未使用の差込口数が電源タップのポート数以上になるまで
    while B >= A:
        # 未使用の差込口数を電源タップのポート数増やす
        B -= A - 1
        # 電源タップの個数をカウントアップ
        cnt += 1
    # 電源タップの個数を出力
    print(cnt)
