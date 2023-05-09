def main():
    N = int(input())
    D = list(map(int, input().split()))
    D.sort()
    #print(D)
    # Kを決めると、K以上の数がARC用の問題となる
    # K未満の数がABC用の問題となる
    # Kを決めるとABC用の問題の数は、K以上の数の個数となる
    # Kを決めるとARC用の問題の数は、K未満の数の個数となる
    # Kを決めるとARC用の問題の数とABC用の問題の数が同じになるとは、
    # K以上の数の個数とK未満の数の個数が同じになるということ
    # ARC用の問題の数を求める
    arc_count = 0
    for i in range(N):
        if D[i] >= D[N//2]:
            arc_count += 1
    # ABC用の問題の数を求める
    abc_count = 0
    for i in range(N):
        if D[i] < D[N//2]:
            abc_count += 1
    # ARC用の問題の数とABC用の問題の数が同じになるKの個数を求める
    if arc_count == abc_count:
        print(0)
    else:
        print(D[N//2] - D[N//2-1])

if __name__ == '__main__':
    main()