def main():
    N = int(input())
    K = int(input())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #print(N, K, P, C)
    #print(len(P), len(C))
    max_sum = -10**9
    for i in range(N):
        #print(i)
        #print('P[i] = ', P[i])
        #print('C[i] = ', C[i])
        #print('max_sum = ', max_sum)
        #print('K = ', K)
        #print('P[P[i]-1] = ', P[P[i]-1])
        #print('C[P[i]-1] = ', C[P[i]-1])
        sum = 0
        j = i
        for _ in range(K):
            sum += C[P[j]-1]
            j = P[j]-1
            if sum > max_sum:
                max_sum = sum
            if j == i:
                break
    print(max_sum)

if __name__ == '__main__':
    main()