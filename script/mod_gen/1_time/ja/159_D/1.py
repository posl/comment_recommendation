def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] += 1
    for i in range(N):
        if B[i] == 1:
            print(0)
        else:
            print(B[i] * (B[i] - 1) // 2)

if __name__ == '__main__':
    main()