def main():
    N = int(input())
    A = list(map(int, input().split()))
    R = [0] * N
    for i in range(N):
        R[i] = A[i] * 2
    for i in range(N):
        R[i] -= R[i - 1]
    print(' '.join(map(str, R)))

if __name__ == '__main__':
    main()