def main():
    # 整数の入力
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a)-min(a))

if __name__ == '__main__':
    main()