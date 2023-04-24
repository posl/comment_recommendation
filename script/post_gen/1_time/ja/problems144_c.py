Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N == 2:
        print(1)
        return
    if N == 3:
        print(2)
        return
    if N == 4:
        print(2)
        return
    if N == 5:
        print(3)
        return

    #i+jの最大値を探す
    i = 1
    j = 1
    while True:
        if i * j > N:
            break
        i += 1
        j += 1
    i -= 1
    j -= 1

    #Nがi*jの中央にあるかどうか
    if N == i * j:
        print(i + j - 2)
        return
    if N == i * j + i:
        print(i + j - 1)
        return
    if N == i * j + j:
        print(i + j - 1)
        return
    if N == i * j + i + j:
        print(i + j)
        return

    #Nがi*jの中央にない場合
    if N < i * j + i:
        print(i + j - 1)
        return
    if N < i * j + j:
        print(i + j - 1)
        return
    if N < i * j + i + j:
        print(i + j)
        return

=======
Suggestion 2

def main():
    N = int(input())
    i = 1
    j = 1
    while True:
        if i * j >= N:
            break
        if i < j:
            i += 1
        else:
            j += 1
    print(i + j - 2)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    while N > 1:
        N = (N + 1) // 2
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    x = 0
    y = 0
    ans = 0
    while True:
        ans += 1
        if x < y:
            x += 1
        else:
            y += 1
        if x * y >= N:
            break
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    x = 1
    y = 1
    cnt = 1
    while cnt < N:
        if x == y:
            x += 1
        else:
            y += 1
        cnt += 1
    print(x+y-1)

=======
Suggestion 6

def main():
    N = int(input())

    # パターン1
    # まずは、Nが書かれているマスに到達するまでに必要な移動回数の最小値を求める
    # 例えば、N=10の場合、
    # 1 2 3 4 5
    # 2 4 6 8 10
    # 3 6 9 12 15
    # 4 8 12 16 20
    # 5 10 15 20 25
    # となるので、N=10の場合、(2,5)に到達するまでに必要な移動回数は、
    # 5回である。
    # また、N=50の場合、(5,10)に到達するまでに必要な移動回数は、
    # 13回である。
    # これを一般化すると、
    # N=10の場合、(2,5)に到達するまでに必要な移動回数は、
    # 5回である。
    # N=50の場合、(5,10)に到達するまでに必要な移動回数は、
    # 13回である。
    # N=100の場合、(10,10)に到達するまでに必要な移動回数は、
    # 20回である。
    # となる。
    # つまり、N=10の場合、(2,5)に到達するまでに必要な移動回数は、
    # 5回である。
    # N=50の場合、(5,10)に到達するまでに必要な移動回数は、
    # 13回である。
    # N=100の場合、(10,10)に到達するまでに必要な移動回数は、
    # 20回

=======
Suggestion 7

def main():
    N = int(input())
    print(N-1)

=======
Suggestion 8

def main():
    N = int(input())
    # N = 100

=======
Suggestion 9

def main():
    N = int(input())
    # 0,0 からの移動回数
    cnt = 0
    # 現在地
    now = (0,0)
    while True:
        # 今いるマスの数字
        num = now[0] * now[1]
        # 今いるマスの数字が N 以上ならば、そこに移動する
        if num >= N:
            break
        # 今いるマスの数字が N より小さいならば、右に移動するか下に移動するかを決める
        else:
            # 今いるマスの数字が 0 ならば、右に移動する
            if num == 0:
                now = (now[0] + 1, now[1])
            # 今いるマスの数字が 0 でないならば、右に移動するか下に移動するかを決める
            else:
                # 右に移動したときのマスの数字
                num_r = now[0] * (now[1] + 1)
                # 下に移動したときのマスの数字
                num_d = (now[0] + 1) * now[1]
                # 右に移動したときのマスの数字が N 以上ならば、下に移動する
                if num_r >= N:
                    now = (now[0], now[1] + 1)
                # 右に移動したときのマスの数字が N より小さいならば、下に移動したときのマスの数字が N 以上ならば、右に移動する
                elif num_d >= N:
                    now = (now[0] + 1, now[1])
                # 右に移動したときのマスの数字と下に移動したときのマスの数字が N より小さいならば、どちらに移動してもよい
                else:
                    # 右に移動したときのマスの数字が下

=======
Suggestion 10

def solve(n):
    # 1 から n までの和を求める
    def sum(n):
        return (1 + n) * n // 2
    # n が書かれているマスに到達するまでに必要な移動回数の最小値を求める
    def count(n):
        if n == 1:
            return 0
        # n が書かれているマスに到達するまでに必要な移動回数の最小値
        count = 0
        # 1 から n までの和
        s = 0
        # 1 から n までの和が n 未満になるまで繰り返す
        while s < n:
            # 1 から n までの和を n で割った商を求める
            # 1 から n までの和が n 未満になるまで繰り返す
            while s < n:
                # 1 から n までの和を n で割った商を求める
                s = sum(n // (count + 1))
                # 1 から n までの和が n 未満になるまで繰り返す
                if s < n:
                    # 1 から n までの和を n で割った商を求める
                    count += 1
        return count
    # n が書かれているマスに到達するまでに必要な移動回数の最小値を求める
    return count(n)
