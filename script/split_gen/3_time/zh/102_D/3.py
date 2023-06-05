def main():
    N = int(input())
    A = list(map(int,input().split()))
    A_sum = sum(A)
    A_cumsum = [0]
    for i in range(N):
        A_cumsum.append(A_cumsum[i]+A[i])
    A_cumsum2 = [0]
    for i in range(N):
        A_cumsum2.append(A_cumsum2[i]+A[i]**2)
    ans = A_sum
    for i in range(1,N-2):
        for j in range(i+1,N-1):
            P = A_cumsum[i]
            Q = A_cumsum[j]-A_cumsum[i]
            R = A_cumsum[N]-A_cumsum[j]
            S = A_sum-P-Q-R
            ans = min(ans,max(P,Q,R,S)-min(P,Q,R,S))
    print(ans)
main()
