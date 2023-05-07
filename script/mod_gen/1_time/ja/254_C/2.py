def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #Aを昇順に並べ替えることが出来るかどうかを判定してください。
    #Aを昇順に並べ替えることが出来たらYes、出来なかったらNoを出力してください。
    if K % 2 == 0:
        for i in range(N-K):
            if A[i] > A[i+K]:
                print('No')
                exit()
        print('Yes')
    else:
        for i in range(N-K):
            if A[i] > A[i+K]:
                print('No')
                exit()
        print('Yes')

if __name__ == '__main__':
    main()