Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # A 匹のスライムがいます。
    # すぬけくんが 1 回叫ぶたびに、スライムは K 倍に増殖します。
    # スライムが B 匹以上になるには、すぬけくんは最小で何回叫ぶ必要があるでしょうか？
    A, B, K = map(int, input().split())

    # スライムの数が B に達するまでの回数を求める
    count = 0
    while A < B:
        A *= K
        count += 1

    # スライムの数が B に達するまでの回数が K 回未満なら、
    # スライムの数が B に達するまでの回数を出力する
    if count < K:
        print(count)
    # スライムの数が B に達するまでの回数が K 回以上なら、
    # スライムの数が B に達するまでの回数を K 回減らした回数を出力する
    else:
        print(count - K)

=======
Suggestion 2

def main():
    A, B, K = map(int, input().split())
    count = 0
    while True:
        if A >= B:
            break
        A *= K
        count += 1
    print(count)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    for i in range(K):
        if A % 2 == 1:
            A -= 1
        A //= 2
        B += A
    print(A, B)

=======
Suggestion 4

def main():
    A,B,K = map(int,input().split())
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)

=======
Suggestion 5

def main():
    a,b,k = map(int, input().split())
    count = 0
    while a < b:
        a *= k
        count += 1
    print(count)

=======
Suggestion 6

def main():
    a, b, k = map(int, input().split())
    if a >= b:
        print(0)
        return
    for i in range(k):
        if a * 2 < b:
            a *= 2
        else:
            a += b
            print(a - b)
            return
    print(a - b)

=======
Suggestion 7

def main():
    a, b, k = map(int, input().split())
    if a >= b:
        print(0)
    else:
        print(max(0, min(b - a - 1, k)))

=======
Suggestion 8

def main():
    A, B, K = map(int, input().split())

    if A >= B:
        print(0)
    else:
        print(min(B-A, K))

=======
Suggestion 9

def main():
    a, b, k = map(int, input().split())
    count = 0
    for i in range(k):
        if a >= b:
            break
        elif a % 2 == 0:
            a = a // 2
            b = b - a
            count += 1
        else:
            a = a // 2 + 1
            b = b - a
            count += 1
    print(count)

=======
Suggestion 10

def main():
    A, B, K = map(int, input().split())
    if B // A >= K:
        print(K)
    else:
        print(B // A)
