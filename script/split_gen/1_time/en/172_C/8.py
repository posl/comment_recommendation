def main():
    #入力
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #累積和
    A_cumsum = [0]
    B_cumsum = [0]
    for i in range(N):
        A_cumsum.append(A_cumsum[i]+A[i])
    for i in range(M):
        B_cumsum.append(B_cumsum[i]+B[i])
    #Bの累積和がKを超える場所を探す
    B_cumsum = [i for i in B_cumsum if i <= K]
    #Aの累積和がKを超える場所を探す
    ans = 0
    for i in range(N+1):
        if A_cumsum[i] > K:
            break
        #Bの累積和がKを超える場所を探す
        j = binary_search(B_cumsum, K-A_cumsum[i])
        ans = max(ans, i+j)
    print(ans)
