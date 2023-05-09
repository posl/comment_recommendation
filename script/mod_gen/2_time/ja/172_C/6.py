def main():
    # input
    N, M, K = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    # compute
    # 机 A に積まれている本の累積和を計算
    As = [0] + list(accumulate(As))
    # 机 B に積まれている本の累積和を計算
    Bs = [0] + list(accumulate(Bs))
    # 机 A に積まれている本の数を計算
    n = bisect.bisect_right(As, K)
    # 机 B に積まれている本の数を計算
    m = bisect.bisect_right(Bs, K)
    # 机 A に積まれている本の数を減らしながら、机 B に積まれている本の数を増やす
    for i in range(n):
        j = bisect.bisect_right(Bs, K-As[i])
        m = max(m, i+j)
    # output
    print(m)

if __name__ == '__main__':
    main()