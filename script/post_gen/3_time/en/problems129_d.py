Synthesizing 1/10 solutions

=======
Suggestion 1

def solve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    # 各マスから見ていって、上下左右にいくつ#があるかを数える
    # その数の最小値が、そのマスから見えるマスの数になる
    # その最小値の最大値が答え
    # ただし、そのマスに#がある場合は、そのマスからは見えないので、0になる
    # また、そのマスが.の場合は、そのマス自身も含めるので、1にな�
