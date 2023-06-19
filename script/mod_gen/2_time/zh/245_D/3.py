def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M+1)
    B[0] = C[0] // A[0]
    for i in range(1, M+1):
        B[i] = (C[i] - sum([A[j] * B[i-j] for j in range(i)])) // A[0]
    print(' '.join(map(str, B)))

if __name__ == '__main__':
    main()