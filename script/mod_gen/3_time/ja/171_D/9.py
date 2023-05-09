def main():
    #N
    N = int(input())
    #A
    A = list(map(int, input().split()))
    #Q
    Q = int(input())
    #B C
    B = [0]*Q
    C = [0]*Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    #Aの合計値
    Asum = sum(A)
    #Bの合計値
    Bsum = [0]*Q
    #Cの合計値
    Csum = [0]*Q
    #Bsumを求める
    for i in range(Q):
        Bsum[i] = B[i]*(A.count(B[i]))
    #Csumを求める
    for i in range(Q):
        Csum[i] = C[i]*(A.count(B[i]))
    #出力
    for i in range(Q):
        Asum = Asum - Bsum[i] + Csum[i]
        print(Asum)

if __name__ == '__main__':
    main()