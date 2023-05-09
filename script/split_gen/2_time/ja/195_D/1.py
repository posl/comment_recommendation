def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        box = X[:L] + X[R+1:]
        box.sort()
        W_sort = sorted(W)
        V_sort = sorted(V)
        print(box)
        print(W_sort)
        print(V_sort)
        #boxの大きさがW_sort[i]以下のものについて、V_sort[i]の価値の和を求める。
        #その中で、最大のものを出力する。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort[i]以下のものは、box内の要素がW_sort[i]以下のものの中で、最大のものを選ぶ。
        #boxの大きさがW_sort
