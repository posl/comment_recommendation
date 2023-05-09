def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    #print(A[1:3])
    sum_A = [0]
    for i in range(N):
        sum_A.append(sum_A[i] + A[i])
    #print(sum_A)
    max_sum = 0
    for i in range(M, N+1):
        #print(i)
        #print(sum_A[i-M:i])
        sum_B = sum_A[i] - sum_A[i-M]
        #print(sum_B)
        if max_sum < sum_B:
            max_sum = sum_B
    #print(max_sum)
    ans = 0
    for i in range(M):
        ans += (i+1) * max_sum
    print(ans)

if __name__ == '__main__':
    main()