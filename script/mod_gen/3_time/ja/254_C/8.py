def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #N=2*Kの時は必ずYes
    if N == 2*K:
        print('Yes')
        return
    #N=2*Kの時以外は、Aを昇順に並べ替えた時の
    #A[i]とA[i+K]が等しいかどうかで判定
    A.sort()
    for i in range(N-K):
        if A[i] == A[i+K]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()