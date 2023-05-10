def main():
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    sum_A = [0]
    sum_B = [0]
    for i in range(N):
        sum_A.append(sum_A[i]+A[i])
    for i in range(M):
        sum_B.append(sum_B[i]+B[i])
    ans = 0
    for i in range(N+1):
        if sum_A[i] > K:
            break
        tmp = i
        for j in range(M+1):
            if sum_A[i] + sum_B[j] > K:
                break
            tmp = i + j
        ans = max(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()