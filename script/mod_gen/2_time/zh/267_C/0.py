def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(M):
        sum += (i+1)*A[i]
    max = sum
    for i in range(M,N):
        sum += (i+1)*A[i] - (i-M+1)*A[i-M]
        if sum > max:
            max = sum
    print(max)

if __name__ == '__main__':
    main()