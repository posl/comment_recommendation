def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # Bの各要素の出現回数を数える
    b_count = {}
    for b in B:
        if b in b_count:
            b_count[b] += 1
        else:
            b_count[b] = 1
    # Aの各要素に対して、b_countの中に対応する要素があれば、その要素の値を出力する
    ans = 0
    for a in A:
        if a in b_count:
            ans += b_count[a]
    print(ans)
