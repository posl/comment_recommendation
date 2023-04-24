Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    if N % (2*D+1) == 0:
        print(N // (2*D+1))
    else:
        print(N // (2*D+1) + 1)

=======
Suggestion 2

def main():
    n, d = map(int, input().split())
    ans = n // (2 * d + 1)
    if n % (2 * d + 1) != 0:
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 4

def main():
    n, d = map(int, input().split())
    print((n + 2 * d) // (2 * d + 1))

=======
Suggestion 5

def main():
    # input
    N, D = map(int, input().split())

    # compute
    ans = N//(2*D+1)
    if N%(2*D+1) != 0:
        ans += 1

    # output
    print(ans)

=======
Suggestion 6

def main():
    # 入力
    N, D = map(int, input().split())

    # 処理
    # 条件を満たすために配置する必要のある監視員の人数の最小値
    min_num = N // (2 * D + 1)
    if N % (2 * D + 1) != 0:
        min_num += 1

    # 出力
    print(min_num)

=======
Suggestion 7

def main():
    #入力
    N, D = map(int, input().split())
    #出力
    print((N + D * 2) // (D * 2 + 1))

=======
Suggestion 8

def main():
    N, D = map(int, input().split())

    # 入力を読み込んで解く
    ans = 0

    # 出力
    print(ans)
