def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    for i in range(N - 1):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])

if __name__ == '__main__':
    main()