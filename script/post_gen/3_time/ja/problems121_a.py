Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H - h) * (W - w))

=======
Suggestion 2

def main():
    # H 行 W 列の白色のマス目があります。
    # あなたは h 個の行と w 個の列を選び、選んだ行または列に含まれるマス目を全て黒色で塗りつぶします。
    # 白色のマス目はいくつ残るでしょうか。
    # なお、残る白色のマス目の数は行や列の選び方によらないことが証明できます。
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H-h)*(W-w))

=======
Suggestion 3

def main():
    # input
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    # compute

    # output
    print((H-h)*(W-w))

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    h2, w2 = map(int, input().split())
    print((h - h2) * (w - w2))
