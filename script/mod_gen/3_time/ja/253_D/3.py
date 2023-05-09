def main():
    #入力
    N,A,B = map(int, input().split())
    #処理
    sum = 0
    for i in range(1,N+1):
        if i % A != 0 and i % B != 0:
            sum += i
    #出力
    print(sum)

if __name__ == '__main__':
    main()