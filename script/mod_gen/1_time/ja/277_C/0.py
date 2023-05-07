def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    if N % 2 == 0:
        print(B[N//2] - A[N//2 - 1] + 1)
    else:
        print(B[N//2] - A[N//2] + 1)

if __name__ == '__main__':
    main()