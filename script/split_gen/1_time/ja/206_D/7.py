def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 1. aを回文にするために必要な操作数を求める
    # 2. 1の操作数が奇数なら、aを回文にできない
    # 3. 1の操作数が偶数なら、aを回文にできる
    # 4. 2の操作数が偶数なら、aを回文にするために必要な操作数は、1の操作数の半分
    # 5. 2の操作数が奇数なら、aを回文にするために必要な操作数は、1の操作数の半分+1
    # 1. aを回文にするために必要な操作数を求める
    # aの要素をキーとして、要素の出現回数を値とする辞書
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    # 出現回数が奇数である要素の数
    odd_count = 0
    for k, v in d.items():
        if v % 2 == 1:
            odd_count += 1
    # 2. 1の操作数が奇数なら、aを回文にできない
    if odd_count % 2 == 1:
        print(-1)
        return
    # 3. 1の操作数が偶数なら、aを回文にできる
    # 4. 2の操作数が偶数なら、aを回文にするために必要な操作数は、1の操作数の半分
    # 5. 2の操作数が奇数なら、aを回文にするために必要な操作数は、1の操作数の半分+1
    print(n - odd_count)
