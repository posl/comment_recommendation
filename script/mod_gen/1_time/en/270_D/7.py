def main():
    #Input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #Process
    result = N
    for i in range(K):
        result -= A[K-1-i]
    #Output
    print(result)

if __name__ == '__main__':
    main()