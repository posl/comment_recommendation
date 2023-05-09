def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        for j in range(1, 2**(N-i)+1):
            if A[2*j-1] > A[2*j]:
                A[2*j-1], A[2*j] = A[2*j], A[2*j-1]
    print(A.index(2))
main()

if __name__ == '__main__':
    main()