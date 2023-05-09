def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    #初期化
    #Aの要素をインデックスに、Aの値を格納する
    #Aの値の最大値はNなので、N+1個の配列を用意する
    B = [[] for _ in range(N+1)]
    for i in range(N):
        B[A[i]].append(i)
    #クエリの処理
    for q in Query:
        l = q[0] - 1
        r = q[1] - 1
        x = q[2]
        #xの値がBのインデックスになっている
        #B[x]の要素は、Aのインデックスになっている
        #B[x]の要素がl以上r以下の範囲にあれば、xの値がAに入っている
        count = 0
        for i in B[x]:
            if l <= i <= r:
                count += 1
        print(count)
