Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, T = map(int, input().split())
    ans = 0
    for i in range(1, T + 1):
        if i % A == 0:
            ans += B
    print(ans)

=======
Suggestion 2

def main():
    a, b, t = map(int, input().split())
    print((t // a) * b)

=======
Suggestion 3

def main():
    a, b, t = map(int, input().split())
    print(b * (t // a))

=======
Suggestion 4

def main():
    A, B, T = map(int, input().split())
    print(B * (T // A))

=======
Suggestion 5

def main():
    #入力
    A, B, T = map(int, input().split())
    #処理
    cnt = 0
    for i in range(1, T+1):
        if i % A == 0:
            cnt += B
    #出力
    print(cnt)

=======
Suggestion 6

def main():
    A, B, T = map(int, input().split())
    if T < A:
        print('0')
    else:
        print(B * (T // A))
