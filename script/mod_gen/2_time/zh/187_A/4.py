def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    sum = 0
    for i in range(1,N):
        sum += A[i] * i - A[i-1] * (N-i)
    print(sum)

if __name__ == '__main__':
    main()