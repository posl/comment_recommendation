def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for _ in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    # A の要素を降順に並び替える
    A.sort(reverse = True)
    # C の要素を降順に並び替える
    C.sort(reverse = True)
    # A の要素を降順に見ていき、C の要素が大きい順に見ていく
    # C の要素が大きい順に見ていくのは、C の要素を降順に並べているから
    # A の要素が大きい順に見ていくのは、A の要素を降順に並べているから
    # A の要素を降順に見ていき、C の要素が大きい順に見ていく
    # C の要素が大きい順に見ていくのは、C の要素を降順に並べているから
    # A の要素が大きい順に見ていくのは、A の要素を降順に並べているから
    # A の要素を降順に見ていき、C の要素が大きい順に見ていく
    # C の要素が大きい順に見ていくのは、C の要素を降順に並べているから
    # A の要素が大きい順に見ていくのは、A の要素を降順に並べているから
    # A の要素を降順に見ていき、C の要素が大きい順に見ていく
    # C の要素が大きい順に見てい
