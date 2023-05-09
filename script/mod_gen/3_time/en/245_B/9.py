def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 0~2000までの配列を用意
    # (0,0,0,...,0)のように初期化
    count = [0 for i in range(2001)]
    # Aの各要素に対して
    # countのその要素の値を1増やす
    for a in A:
        count[a] += 1
    # countの各要素に対して
    # 0でなければその要素の値を出力して終了
    for i in range(2001):
        if count[i] == 0:
            print(i)
            return

if __name__ == '__main__':
    main()