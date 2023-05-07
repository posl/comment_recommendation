def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    #Aの要素の値をキーに、その要素のインデックスを値とする辞書を作成
    #例えば、A = [3,1,4,1,5]の場合、
    #A_dict = {3:0, 1:1, 4:2, 5:4}となる
    A_dict = {A[i]:i for i in range(N)}
    Q_list = []
    for i in range(Q):
        Q_list.append([int(x) for x in input().split()])
    #Q_list[i] = [L,R,X]
    #L,Rはインデックスで表されるので、実際の要素の値を取得するためには、
    #L-1,R-1とする
    for i in range(Q):
        L = Q_list[i][0]-1
        R = Q_list[i][1]-1
        X = Q_list[i][2]
        #XがAの要素の値として存在するかどうかをチェック
        if X in A_dict:
            #存在する場合、Xのインデックスを取得
            X_index = A_dict[X]
            #L以上R以下のインデックスにX_indexが含まれるかどうかをチェック
            if L <= X_index <= R:
                #含まれる場合、Xを含む要素の個数はR-L+1
                print(R-L+1)
            else:
                #含まれない場合、Xを含む要素の個数はR-L
                print(R-L)
        else:
            #存在しない場合、Xを含む要素の個数は0
            print(0)

if __name__ == '__main__':
    main()