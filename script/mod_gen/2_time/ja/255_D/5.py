def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # Aの要素を全てXにするのに必要な最小の操作回数を求める
    # 操作は2通りある
    # A_iから1を減算する
    # A_iに1を加算する
    # どちらを選んでも結果は変わらないので、A_iとXの差が奇数なら1回、偶数なら0回の操作をする
    # 0回の操作は必要ないので、全てのA_iとXの差が奇数の場合のみ考える
    # また、A_iとXの差は最大でも10^9なので、差が奇数の個数は10^9以下
    # そのため、差が奇数の個数を求める
    # この個数を全てのA_iに対して足し合わせると、最小の操作回数が求まる
    # まず、差が奇数の個数を求める
    odd_count = 0
    for a, x in zip(A, X):
        if (a - x) % 2 == 1:
            odd_count += 1
    # その個数を全てのA_iに対して足し合わせる
    for a in A:
        print(odd_count)

if __name__ == '__main__':
    main()