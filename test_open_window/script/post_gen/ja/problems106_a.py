Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    a, b = map(int, input().split())
    print((a - 1) * (b - 1))

=======

def main():
    a, b = map(int, input().split())
    print(a * b - (a + b - 1))

=======

def main():
    A, B = map(int, input().split())
    print(A * B - (A + B - 1))

=======

def main():
    a, b = map(int, input().split())
    print((a-2)*(b-2))

=======

def main():
    # 入力
    A, B = map(int, input().split())

    # 道を除いた畑の面積を求める
    ans = A * B - (A + B - 1)

    # 出力
    print(ans)
