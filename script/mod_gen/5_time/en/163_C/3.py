def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0] * N
    for i in range(1, N):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])

if __name__ == '__main__':
    main()