def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - A[i-1]
    print(*A)
main()

if __name__ == '__main__':
    main()