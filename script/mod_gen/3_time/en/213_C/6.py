def main():
    H, W, N = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    A, B = zip(*AB)
    A = list(A)
    B = list(B)
    A.sort()
    B.sort()
    A = [i for i, v in enumerate(A)]
    B = [i for i, v in enumerate(B)]
    for i in range(N):
        print(A[i]+1, B[i]+1)

if __name__ == '__main__':
    main()