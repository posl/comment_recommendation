def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(N):
        B[i] = (i+1)*A[i] - (N-i)*A[i]
    B.sort(reverse=True)
    print(sum(B[:M]))

if __name__ == '__main__':
    main()