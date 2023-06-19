def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(1, N):
        A[i] %= A[0]
        if A[i] == 0:
            A[i] = A[0]
    A[0] = 0
    A.sort()
    print(A[0])

if __name__ == '__main__':
    main()