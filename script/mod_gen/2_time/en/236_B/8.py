def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #count
    B = [0]*N
    for i in range(4*N-1):
        B[A[i]-1] += 1
    #output
    for i in range(N):
        if B[i] % 2 == 1:
            print(i+1)

if __name__ == '__main__':
    main()