def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(2*N+1)
    for i in range(N):
        B[A[i]] = i+1
    for i in range(1, 2*N+1):
        j = B[i]
        print(0 if j==1 else 1+B[j//2])
main()

if __name__ == '__main__':
    main()