def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = list(enumerate(A))
    A = sorted(A, key=lambda x: x[1], reverse=True)
    A = A[:(1 << N)]
    A = sorted(A, key=lambda x: x[0])
    print(A[1][0] + 1)

if __name__ == '__main__':
    main()