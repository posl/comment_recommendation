def main():
    N = int(input())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(N-1):
        for j in range(i+1,N):
            sum += abs(A[i]-A[j])
    print(sum)

if __name__ == '__main__':
    main()