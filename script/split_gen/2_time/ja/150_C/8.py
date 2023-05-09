def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    import itertools
    from itertools import permutations
    #順列の生成
    li = []
    for i in range(1, N+1):
        li.append(i)
    #順列の生成
    li = list(permutations(li))
    #print(li)
    #順列を辞書順に並び替える
    li.sort()
    #print(li)
    #P,Qの順列を辞書順に並び替える
    P.sort()
    Q.sort()
    #print(P)
    #print(Q)
    #P,Qの順列の辞書順の番号を取得
    a = li.index(tuple(P)) + 1
    b = li.index(tuple(Q)) + 1
    #print(a)
    #print(b)
    #答えを出力
    print(abs(a - b))
