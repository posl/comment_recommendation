def main():
    N = int(input())
    # Nを2進数で表記した時、1となる位は15個以下である
    # 0から15までの2進数を作成する
    for i in range(2**15):
        # 2進数を10進数に変換
        x = int(bin(i)[2:])
        # 2進数を10進数に変換したときにNと一致しない場合はスキップ
        if x > N:
            continue
        # 2進数を10進数に変換したときにNと一致する場合は出力
        if x == N:
            print(x)
            continue
        # 2進数を10進数に変換したときにNと一致しない場合はスキップ
        if x < N:
            # 2進数を10進数に変換したときにNと一致する場合は出力
            if x & N == x:
                print(x)

if __name__ == '__main__':
    main()