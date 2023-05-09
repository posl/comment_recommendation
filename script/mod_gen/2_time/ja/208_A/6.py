def main():
    # A, B = map(int, input().split())
    A, B = 2, 11
    # 1,2,...,6 の出目がある 6 面サイコロを A 回振ったとき、出た目の合計が B になることはありますか？
    # 6 ** A 通りの出目の組み合わせを全部試す
    # 6 ** A 通り試すのは無理なので、A 回振ったときに出る出目の和の最小値と最大値を求める
    # 最小値は A * 1、最大値は A * 6
    # 最小値が B より大きい場合は No
    # 最大値が B より小さい場合は No
    # 最小値と最大値の間に B があれば Yes
    # どれにも当てはまらない場合は No
    # 最小値
    min_sum = A * 1
    # 最大値
    max_sum = A * 6
    if B < min_sum or max_sum < B:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()