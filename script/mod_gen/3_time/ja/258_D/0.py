def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #AとBの合計時間を計算
    AB = [a + b for a, b in zip(A, B)]
    #Aの合計時間を計算
    A_sum = sum(A)
    #Bの合計時間を計算
    B_sum = sum(B)
    #Aの合計時間がXを超えている場合
    if A_sum >= X:
        #Aの合計時間がXを超えるまで、Bの合計時間を引く
        for i in range(N):
            if A_sum >= X:
                A_sum -= B[i]
            else:
                break
        #Aの合計時間がXを超えた後に、Aの合計時間がXを超えるまで、Aの合計時間を引く
        for i in range(N):
            if A_sum >= X:
                A_sum -= A[i]
            else:
                break
        #Aの合計時間がXを超えた後に、Aの合計時間がXを超えるまで、Bの合計時間を引く
        for i in range(N):
            if A_sum >= X:
                A_sum -= B[i]
            else:
                break
        #Aの合計時間がXを超えた後に、Aの合計時間がXを超えるまで、Aの合計時間を引く
        for i in range(N):
            if A_sum >= X:
                A_sum -= A[i]
            else:
                break
        #Aの合計時間がXを超えた後に、Aの合計時間がXを超えるまで、Bの合計時間を引く
        for i in range(N):
            if A_sum >= X:
                A_sum -= B[i]
            else:
                break
        #Aの合計時間がXを超えた後に、Aの合計時間がXを超えるまで、Aの合計時間を引く
        for i

if __name__ == '__main__':
    main()