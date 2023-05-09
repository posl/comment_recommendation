def main():
    X, K, D = map(int, input().split())
    # XをDで割った商
    q = X // D
    # XをDで割った余り
    r = X % D
    # qがK以下ならば、Dの倍数の移動をK回繰り返すことで、Xに近づくことができる
    if q <= K:
        # Kからqを引いた値が偶数ならば、Xの絶対値はrで決まる
        if (K - q) % 2 == 0:
            print(abs(r))
        # Kからqを引いた値が奇数ならば、Xの絶対値はD-rで決まる
        else:
            print(abs(D - r))
    # qがKより大きいならば、Dの倍数の移動をq回繰り返した後に、Xの絶対値はDで割った余りで決まる
    else:
        print(abs(X - D * K))

if __name__ == '__main__':
    main()