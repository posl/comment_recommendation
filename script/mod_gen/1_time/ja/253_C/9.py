def main():
    import sys
    import io
    import os
    from collections import defaultdict
    input = sys.stdin.readline
    N = int(input())
    # この問題は、最大値と最小値を求める問題である。
    # これは、最大値と最小値をO(1)で求められるデータ構造を用いることで解くことができる。
    # この問題では、最大値と最小値を求めることができるsetを用いる。
    # ただし、setは重複を許さないため、重複を許すmultisetを用いる。
    # pythonにはmultisetはないため、defaultdictを用いて実装する。
    # defaultdictは、キーが存在しない場合に、デフォルト値を返すデータ構造である。
    # このデフォルト値は、初期化時に与えることができる。
    # 今回は、キーが存在しない場合に0を返すように設定する。
    # これにより、multisetのように扱うことができる。
    # また、multisetを用いると、最大値と最小値を求めることができる。
    # また、multisetは、要素の追加、削除がO(logN)でできる。
    # 今回の問題では、クエリ1は要素の追加、クエリ2は要素の削除、クエリ3は、最大値と最小値の差を出力する。
    # クエリ1の場合、要素を追加する。
    # クエリ2の場合、要素を削除する。
    # ただし、要素を削除する際には

if __name__ == '__main__':
    main()