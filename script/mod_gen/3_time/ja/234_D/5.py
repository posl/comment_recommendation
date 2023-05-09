def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    P = [i-1 for i in P]
    #print(P)
    # 累積和
    S = [0]
    for i in P:
        S.append(S[-1] + i)
    #print(S)
    # おなじ数字を含む累積和
    # 例えば、[1, 2, 1, 1, 1] なら [1, 2, 3, 4, 5]
    S2 = [0]
    for i in P:
        S2.append(S2[-1] + i + 1)
    #print(S2)
    # おなじ数字を含む累積和の差分
    # 例えば、[1, 2, 1, 1, 1] なら [1, 1, 0, 0, 0]
    S3 = [0]
    for i in P:
        S3.append(S3[-1] + i + 1 - S2[-1] + S2[-i-2])
    #print(S3)
    for i in range(K, N+1):
        #print(i)
        #print(S[i] - S[i-K])
        #print(S2[i] - S2[i-K])
        #print(S3[i] - S3[i-K])
        print(S[i] - S[i-K] - S3[i] + S3[i-K])

if __name__ == '__main__':
    main()