def main():
    n, x = map(int, input().split())
    # 入力された文字列をアルファベットのリストに変換
    alphabet = list(map(chr, range(65, 91)))
    # 入力された文字列のアルファベットの数をリストに格納
    list = []
    for i in range(n):
        list.append(x // n)
        x = x % n
    # 入力された文字列のアルファベットの数をリストに追加
    for i in range(x):
        list[i] += 1
    # アルファベットのリストとアルファベットの数をリストを結合
    result = list(zip(alphabet, list))
    # 結合したリストを文字列に変換
    result = ''.join([''.join(x) for x in result])
    print(result[x - 1])
