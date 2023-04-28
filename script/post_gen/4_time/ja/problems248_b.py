Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    cnt = 0
    while a < b:
        a *= k
        cnt += 1
    print(cnt)

=======
Suggestion 2

def solve():
    A, B, K = map(int, input().split())
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)

=======
Suggestion 3

def solve():
    A, B, K = map(int, input().split())
    cnt = 0
    while A < B:
        A *= K
        cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    a, b, k = map(int, input().split())
    cnt = 0
    while a < b:
        a = a * k
        cnt += 1
    print(cnt)

=======
Suggestion 5

def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    a, b, k = map(int, input().split())
    # スペース区切りの整数の入力
    #a, b, k = map(int, input().split())
    # 文字列の入力
    #s = input()
    # 出力
    #print("{}

=======
Suggestion 6

def main():
    a,b,k = map(int,input().split())
    count = 0
    while a < b:
        a *= k
        count += 1
    print(count)

=======
Suggestion 7

def main():
    a,b,k = map(int,input().split())
    cnt = 0
    while a <= b:
        a *= k
        cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    A, B, K = map(int, input().split())

    cnt = 0
    while B > A:
        A *= K
        cnt += 1

    print(cnt)

=======
Suggestion 9

def func(a, b, k):
    cnt = 0
    while True:
        if a >= b:
            break
        a *= k
        cnt += 1
    return cnt
