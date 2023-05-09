def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append(A[i] + i + 1)
    B.sort(reverse=True)
    print(sum(B[0:M]))

if __name__ == '__main__':
    main()