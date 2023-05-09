def main():
    #入力
    N = int(input())
    A = [int(input()) for _ in range(N)]
    #Aの最大値を求める
    maxA = max(A)
    #Aの最大値のインデックスを求める
    maxA_index = A.index(maxA)
    #Aの最大値を除いた最大値を求める
    maxA2 = max(A[:maxA_index] + A[maxA_index+1:])
    #出力
    for i in range(N):
        if i == maxA_index:
            print(maxA2)
        else:
            print(maxA)

if __name__ == '__main__':
    main()