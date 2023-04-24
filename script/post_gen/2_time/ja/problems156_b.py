Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    while N > 0:
        N //= K
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    ans = 0
    while N > 0:
        ans += 1
        N //= K
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    i = 0
    while n > 0:
        n //= k
        i += 1
    print(i)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    print(len(str(N)))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    print(len(str(n)))

=======
Suggestion 6

def main():
    #入力
    N, K = map(int, input().split())
    #処理
    ans = 0
    while N > 0:
        N //= K
        ans += 1
    #出力
    print(ans)

=======
Suggestion 7

def main():
    # 入力
    n, k = map(int, input().split())
    # 処理
    ans = len(str(n))
    # 出力
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    print(len(str(N)) * K)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    print(len(str(N).encode('utf-8')) * 8 // int(math.log2(K)))

main()

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    print(len(str(N)))
    print(len(str(N).replace("0", "")))
    print(len(str(N).replace("0", "")) + 1)
