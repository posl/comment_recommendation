def main():
    n = int(input())
    v = list(map(int, input().split()))
    #print(n)
    #print(v)
    #偶数番目の数列
    evens = v[0::2]
    #print(evens)
    #奇数番目の数列
    odds = v[1::2]
    #print(odds)
    #偶数番目の数列の中で一番多い数
    even_max = max(evens, key=evens.count)
    #print(even_max)
    #奇数番目の数列の中で一番多い数
    odd_max = max(odds, key=odds.count)
    #print(odd_max)
    #偶数番目の数列の中で一番多い数の個数
    even_max_count = evens.count(even_max)
    #print(even_max_count)
    #奇数番目の数列の中で一番多い数の個数
    odd_max_count = odds.count(odd_max)
    #print(odd_max_count)
    #偶数番目の数列の中で一番多い数の個数と奇数番目の数列の中で一番多い数の個数の和
    even_odd_sum = even_max_count + odd_max_count
    #print(even_odd_sum)
    #偶数番目の数列の中で一番多い数の個数と奇数番目の数列の中で一番多い数の個数の和が偶数の場合
    if even_odd_sum % 2 == 0:
        #偶数番目の数列の中で一番多い数の個数と奇数番目の数列の中で一番多い数の個数の和の半分
        half_even_odd_sum = even_odd_sum // 2
        #print(half_even_odd_sum)
        #偶数番目の数列の中で一番多い数の個数と奇数番目の数列の中で一番多い数の個数の和の半分

if __name__ == '__main__':
    main()