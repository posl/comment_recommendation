def solve():
    N = int(input())
    d = list(map(int, input().split()))
    # 2つ選ぶ方法はN*(N-1)/2通り
    # そのそれぞれについて、一緒に食べたときの体力の回復量を求める
    # その総和を出力する
    # 体力の回復量は、おいしさの積
    # おいしさの積を求めるのに、2重ループを回す
    # 2重ループの中で、おいしさの積を求めて、総和を取る
    # 2重ループの中で、おいしさの積を求めるには、
    # おいしさのリストをソートして、小さい順に取り出して、
    # おいしさの積を求める
    # おいしさのリストをソートするには、sorted を使う
    d_sorted = sorted(d)
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d_sorted[i] * d_sorted[j]
    print(sum)
