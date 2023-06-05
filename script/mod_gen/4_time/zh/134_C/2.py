def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    max = A[N-1]
    for i in range(N):
        if A[i] < max:
            print(max)
        else:
            print(A[N-2])

if __name__ == '__main__':
    main()