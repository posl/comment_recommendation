def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #Aの最小値
    a_min = min(A)
    #Aの最大値
    a_max = max(A)
    #Aの最大値以下の偶数の最大値
    a_max_even = a_max//2*2
    #Aの最小値以下の偶数の最大値
    a_min_even = a_min//2*2
    #Aの最大値以下の偶数の最大値以下の整数の最大値
    a_max_even_max = a_max_even//2
    #Aの最小値以下の偶数の最大値以下の整数の最大値
    a_min_even_max = a_min_even//2
    #Aの最大値以下の偶数の最大値以下の整数の最大値以下の整数の最大値
    a_max_even_max_max = a_max_even_max//2
    #Aの最小値以下の偶数の最大値以下の整数の最大値以下の整数の最大値
    a_min_even_max_max = a_min_even_max//2
    #Aの最大値以下の偶数の最大値以下の整数の最大値以下の整数の最大値以下の整数の最大値
    a_max_even_max_max_max = a_max_even_max_max//2
    #Aの最小値以下の偶数の最大値以下の整数の最大値以下の整数の最大値以下の整数の最大値
    a_min_even_max_max_max = a_min_even_max_max//2
    #Aの最大値以下��

if __name__ == '__main__':
    main()