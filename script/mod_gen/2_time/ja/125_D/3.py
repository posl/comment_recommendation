def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] * n
    B[0] = A[0]
    B[n-1] = A[n-1]
    for i in range(1, n-1):
        B[i] = A[i] + A[i-1]
    B.sort()
    print(sum(B))

if __name__ == '__main__':
    main()