def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    sum = 0
    for i in range(N-1):
        for j in range(i+1,N):
            sum += A[i]*A[j]
    print(sum%(10**9+7))

if __name__ == '__main__':
    main()