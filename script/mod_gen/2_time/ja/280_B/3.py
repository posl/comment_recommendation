def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    for i in range(N):
        A[i] = S[i] - sum(A[:i])
    print(*A)

if __name__ == '__main__':
    main()