def main():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    current = N
    for i in range(M):
        current -= A[i] - B[i-1] if i > 0 else A[i]
        if current <= 0:
            print('No')
            return
        current += B[i] - A[i]
        if current > N:
            current = N
    current -= T - B[-1]
    print('Yes' if current > 0 else 'No')
main()

if __name__ == '__main__':
    main()