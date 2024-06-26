def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    # 魔法は整数の組 (a,b) によって識別されていて、地点 (x,y) にいるときに魔法 (a,b) を使うと (x+a,y+b) にワープする
    # すぬけ君は、任意の整数の組 (a,b) を選んで魔法 (a,b) を覚えることができる大魔術師
    # すぬけ君は何種類でも魔法を覚えることができる
    # 魔法を使って街と街の間を移動したくなったすぬけ君は、全ての相異なる街の組 (i,j) について次の行動を取れるようにいくつかの魔法を覚えることにしました。
    # 覚えた魔法のうち 1 種類の魔法のみ を選ぶ。その後、選んだ魔法 のみ を繰り返し使って街 i から 街 j に移動する。
    # すぬけ君が上の条件を満たすように魔法を覚えるとき、少なくとも何種類の魔法を覚えればよいか？
    # 2 ≦ N ≦ 500
    # 0 ≦ x_i ≦ 10^9 (1 ≦ i ≦ N)
    # 0 ≦ y_i ≦ 10^9 (1 ≦ i ≦ N)
    # i ≠ j ならば (x_i, y_i) ≠ (x_j, y_j) である。
    # 同じ
