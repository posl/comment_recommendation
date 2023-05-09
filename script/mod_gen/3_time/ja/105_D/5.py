def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    # 累積和を求める
    cumsum = [0]
    for a in A:
        cumsum.append((cumsum[-1] + a) % M)
    # 累積和のリストから、同じ値が何個あるかをカウントする
    # 例えば、[0, 1, 1, 2, 2, 2, 3, 3, 4] なら、
    # 0: 1個、1: 2個、2: 3個、3: 2個、4: 1個
    from collections import Counter
    count = Counter(cumsum)
    # 組み合わせの数を求める
    # 例えば、[0, 1, 1, 2, 2, 2, 3, 3, 4] なら、
    # 0: 1個、1: 2個、2: 3個、3: 2個、4: 1個
    # から 1個、2個、3個の組み合わせの総和を求める
    ans = 0
    for v in count.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()