def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0]*N
    A[0] = B[0]
    for i in range(1, N-1):
        A[i] = max(B[i], B[i-1])
    A[-1] = B[-1]
    print(sum(A))

if __name__ == '__main__':
    main()