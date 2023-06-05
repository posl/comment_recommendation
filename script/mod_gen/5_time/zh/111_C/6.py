def main():
    n = int(input())
    v = list(map(int, input().split()))
    #奇数番目と偶数番目に分ける
    odd = [0] * 100001
    even = [0] * 100001
    for i in range(n):
        if i % 2 == 0:
            even[v[i]] += 1
        else:
            odd[v[i]] += 1
    #最も多く現れる数字を探す
    max_odd = 0
    max_even = 0
    max_odd_idx = 0
    max_even_idx = 0
    for i in range(100001):
        if max_odd < odd[i]:
            max_odd = odd[i]
            max_odd_idx = i
        if max_even < even[i]:
            max_even = even[i]
            max_even_idx = i
    #最も多く現れる数字が異なる場合は、それらを除いて置換する
    if max_odd_idx != max_even_idx:
        print(n - max_odd - max_even)
    #最も多く現れる数字が同じ場合は、より少なく現れる数字を除いて置換する
    else:
        #最も多く現れる数字を除いた時の最大値を探す
        second_odd = 0
        second_even = 0
        for i in range(100001):
            if i == max_odd_idx:
                continue
            if second_odd < odd[i]:
                second_odd = odd[i]
            if second_even < even[i]:
                second_even = even[i]
        print(n - max(max_odd + second_even, second_odd + max_even))

if __name__ == '__main__':
    main()