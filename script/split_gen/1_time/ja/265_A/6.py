def main():
    # 入力
    X, Y, N = map(int, input().split())
    # 処理
    # 1個のりんごを買うのに必要な金額
    A = X
    # 3個のりんごを買うのに必要な金額
    B = Y
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った商
    C = (B - A) // 2
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った余り
    D = (B - A) % 2
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った商をNで割った商
    E = N // C
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った商をNで割った余り
    F = N % C
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った商をNで割った商に3個のりんごを買うのに必要な金額を掛けた金額
    G = E * B
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った商をNで割った余りに1個のりんごを買うのに必