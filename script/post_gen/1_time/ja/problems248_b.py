Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # A 匹のスライムがいます。
    # すぬけくんが 1 回叫ぶたびに、スライムは K 倍に増殖します。
    # スライムが B 匹以上になるには、すぬけくんは最小で何回叫ぶ必要があるでしょうか？
    # 制約
    # 1 ≦ A ≦ B ≦ 10^9
    # 2 ≦ K ≦ 10^9
    # 入力は全て整数
    # 入力
    # 入力は以下の形式で標準入力から与えられる。
    # A B K
    # 出力
    # 答えを出力せよ。
    # 入力例 1
    # 1 4 2
    # 出力例 1
    # 2
    # はじめ、スライムが 1 匹です。すぬけくんが 1 回叫ぶとスライムは 2 匹になり、 2 回叫ぶとスライムは 4 匹になります。4 匹以上になるためには、最小で 2 回叫ぶ必要があります。
    # 入力例 2
    # 7 7 10
    # 出力例 2
    # 0
    # はじめからスライムは 7 匹です。
    # 入力例 3
    # 31 415926 5
    # 出力例 3
    # 6
    A, B, K = map(int, input().split())
    # print(A, B, K)
    # print(type(A), type(B), type(K))

    # 1 ≦ A ≦ B ≦ 10^9
    # 2 ≦ K ≦ 10^9
    # 入力は全て整数
    # B が

=======
Suggestion 2

def main():
    A, B, K = map(int, input().split())
    cnt = 0
    while A < B:
        A *= K
        cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    for i in range(K):
        if A % 2 == 0:
            A = A // 2
            B = B + A
        else:
            A = (A - 1) // 2
            B = B + (A + 1)
    print(A, B)

=======
Suggestion 4

def main():
    a,b,k = map(int,input().split())
    cnt = 0
    while a < b:
        a *= k
        cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    A,B,K = map(int,input().split())
    ans = 0
    while A < B:
        A *= K
        ans += 1
    print(ans)

main()

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    if B - A <= 2 * K:
        print(0)
    else:
        print(B - A - 2 * K)

main()

=======
Suggestion 7

def main():
    # A, B, K = map(int, input().split())
    A, B, K = 31, 415926, 5
    # A, B, K = 7, 7, 10
    # A, B, K = 1, 4, 2

    # print(A)
    # print(B)
    # print(K)

    # A, B, K = 1, 4, 2
    # A, B, K = 7, 7, 10
    # A,

=======
Suggestion 8

def main():
    A,B,K = map(int,input().split())
    count = 0
    while True:
        if count == K:
            break
        if A % 2 == 1:
            A = A - 1
        A = A / 2
        B = B + A
        count = count + 1
    print(int(A),int(B))

=======
Suggestion 9

def getAns(a,b,k):
    count = 0
    while True:
        if a >= b:
            return count
        a *= k
        count += 1

a,b,k = map(int,input().split())
print(getAns(a,b,k))
