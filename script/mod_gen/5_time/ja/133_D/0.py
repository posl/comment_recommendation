def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - A[i-1]
    print(*B)

if __name__ == '__main__':
    main()