def main():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    #右端でソート
    sort = sorted([(R[i], L[i]) for i in range(N)])
    #右端の最初の値を格納
    right = sort[0][0]
    #左端の最初の値を格納
    left = sort[0][1]
    for i in range(1, N):
        #右端の値が前の左端の値よりも大きい場合
        if right <= sort[i][1]:
            #左端の値を更新
            left = sort[i][1]
            #右端の値を更新
            right = sort[i][0]
        #右端の値が前の左端の値よりも小さい場合
        elif right <= sort[i][0]:
            #右端の値を更新
            right = sort[i][0]
    print(left, right)
