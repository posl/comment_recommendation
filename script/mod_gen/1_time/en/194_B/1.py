def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 1:
        # N is odd
        print(max(A[N//2], B[N//2]))
    else:
        # N is even
        print(max(A[N//2-1]+A[N//2], B[N//2-1]+B[N//2]))

if __name__ == '__main__':
    main()