def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - sum(B) * 2
    print(*B)

if __name__ == '__main__':
    main()