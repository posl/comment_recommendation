def main():
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    sumA = [0]
    sumB = [0]
    for i in range(N):
        sumA.append(sumA[i]+A[i])
    for i in range(M):
        sumB.append(sumB[i]+B[i])
    ans = 0
    j = M
    for i in range(N+1):
        if sumA[i] > K:
            break
        while sumB[j] > K - sumA[i]:
            j -= 1
        ans = max(ans,i+j)
    print(ans)
