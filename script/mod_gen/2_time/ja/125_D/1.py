def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = A[0]
    for i in range(N - 1):
        B[i + 1] = A[i + 1] + B[i]
    B = [abs(b) for b in B]
    print(sum(B))

if __name__ == '__main__':
    main()