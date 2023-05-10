def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    A.sort()
    for i in range(N):
        if i != N-1:
            print(A[N-1])
        else:
            print(A[N-2])

if __name__ == '__main__':
    main()