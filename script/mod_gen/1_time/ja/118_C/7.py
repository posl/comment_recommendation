def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 体力の最小値を出力する
    print(gcd_list(A))

if __name__ == '__main__':
    main()