def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    #正の数の組み合わせ
    plus = []
    #負の数の組み合わせ
    minus = []
    #0の数
    zero = 0
    for i in range(n):
        if a[i] > 0:
            plus.append(a[i])
        elif a[i] < 0:
            minus.append(a[i])
        else:
            zero += 1
    #print(plus)
    #print(minus)
    #print(zero)
    #正の数の組み合わせ
    plus_pair = []
    #負の数の組み合わせ
    minus_pair = []
    #0の数
    zero_pair = 0
    #正の数の組み合わせの数
    plus_pair_num = 0
    #負の数の組み合わせの数
    minus_pair_num = 0
    #0の組み合わせの数
    zero_pair_num = 0
    #正の数の組み合わせの数
    plus_pair_num = ((len(plus) * (len(plus) - 1)) // 2)
    #負の数の組み合わせの数
    minus_pair_num = ((len(minus) * (len(minus) - 1)) // 2)
    #0の組み合わせの数
    zero_pair_num = ((zero * (zero - 1)) // 2)
    #print(plus_pair_num)
    #print(minus_pair_num)
    #print(zero_pair_num)
    #正の数の組み合わせの数
    plus_pair_num = ((len(plus) * (len(plus) - 1)) // 2)
    #負の数の組み合わせの数
    minus_pair_num = ((len(minus) * (len(minus) - 1)) // 2)
    #0の組み合わせの数
    zero_pair_num = ((zero * (zero -
