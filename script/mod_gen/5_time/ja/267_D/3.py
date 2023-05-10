def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    max_sum = 0
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += (j+1)*A[i+j]
        #print(sum)
        if max_sum < sum:
            max_sum = sum
    print(max_sum)

if __name__ == '__main__':
    main()