def main():
    N = int(input())
    #貯金箱の中身の合計
    total = 0
    #何日目の夜か
    day = 0
    #貯金箱の中身の合計がN以上になるまで繰り返す
    while total < N:
        #貯金箱の中身の合計に日数を足す
        total += day
        #日数を1足す
        day += 1
    #日数を出力する
    print(day)

if __name__ == '__main__':
    main()