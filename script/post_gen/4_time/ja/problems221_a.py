Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(32**(a-b))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    ans = 1
    for i in range(B, A):
        ans *= 32
    print(ans)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(32 ** (A - B))

=======
Suggestion 4

def main():
    # 標準入力から値を取得する
    a, b = map(int, input().split())
    # マグニチュードが 1 増える度にエネルギーは約 32 倍になる
    # マグニチュードが 1 増える度に地震のエネルギーがちょうど 32 倍になる
    # マグニチュード A の地震のエネルギーの大きさはマグニチュード B の地震のエネルギーの大きさの何倍ですか?
    print(32**(a-b))
