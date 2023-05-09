def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [abs(x) for x in A]
    #print(A)
    #print(N, K)
    #print(A)
    #0の位置を探す
    zero = 0
    for i in range(N):
        if A[i] == 0:
            zero = i
            break
    #print(zero)
    #0を含まない場合
    if zero == 0:
        #print("0を含まない")
        #積が負の組み合わせの数を求める
        #A[i] * A[j]が負のとき、i < j
        #A[i] * A[j]が負のとき、A[i]が負、A[j]が正
        #A[i]が負のとき、A[i] < 0 かつ A[j] > 0
        #A[j]が正のとき、A[i] < 0 かつ A[j] > 0
        #A[i] < 0 かつ A[j] > 0 のとき、i < j
        #A[i] < 0 かつ A[j] > 0 のとき、A[i] * A[j]が負
        #A[i] < 0 かつ A[j] > 0 のとき、i < j かつ A[i] * A[j]が負
        #A[i] < 0 かつ A[j] > 0 のとき、i < j かつ A[i] * A[j]が負の組み合わせの数は
        #負の数の数 * 正の数の数
        #A[i] < 0 のとき、A[i] < 0 かつ A[j] > 0
        #A[j] > 0 のとき、A[i] < 0 かつ A[j] > 0
        #A[i] < 0 かつ A[j] > 0 のとき、A[i] < 0

if __name__ == '__main__':
    main()