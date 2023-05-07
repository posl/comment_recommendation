def main():
    #入力
    K = int(input())
    #偶数の数
    even = K//2
    #奇数の数
    odd = K - even
    #出力
    print(even * odd)

if __name__ == '__main__':
    main()