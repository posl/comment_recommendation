def main():
    N, X = map(int, input().split())
    #N個の袋の中身をリストに格納
    A = [list(map(int, input().split())) for _ in range(N)]
    #袋の中身を一つずつ取り出す
    for a in A:
        #袋の中身の個数を取得
        L = a.pop(0)
        #袋の中身の数を格納
        a = a
    #袋の中身を全て掛け合わせる
    #全ての袋の中身を掛け合わせた結果を格納するリスト
    A = []
    #袋の中身の個数を格納するリスト
    L = []
    #袋の中身を全て掛け合わせる
    for a in A:
        #袋の中身の個数を取得
        l = a.pop(0)
        #袋の中身の数を格納
        a = a
        #袋の中身の個数を格納
        L.append(l)
        #袋の中身を全て掛け合わせる
        for i in range(0, l):
            for j in range(i + 1, l):
                #袋の中身を全て掛け合わせた結果を格納
                A.append(a[i] * a[j])
    #袋の中身を全て掛け合わせた結果をソート
    A.sort()
    #袋の中身の個数をソート
    L.sort()
    #袋の中身を全て掛け合わせた結果の個数を格納
    l = len(A)
    #袋の中身を全て掛け合わせた結果の個数を格納
    L = len(L)
    #袋の中身を全て掛け合わせた結果の個数を格納

if __name__ == '__main__':
    main()