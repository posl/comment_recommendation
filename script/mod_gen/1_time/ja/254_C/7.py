def main():
    #入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #N, K, Aを確認
    #print(N, K)
    #print(A)
    #Aを昇順に並び替える
    A.sort()
    #Aを確認
    #print(A)
    #K個飛ばしでAを確認
    for i in range(N-K):
        #print(i, A[i], A[i+K])
        #A[i]とA[i+K]が同じならNo
        if A[i] == A[i+K]:
            print('No')
            break
    #A[i]とA[i+K]が全て異なるならYes
    else:
        print('Yes')

if __name__ == '__main__':
    main()