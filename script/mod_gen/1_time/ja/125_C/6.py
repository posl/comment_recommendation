def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_gcd = 0
    for i in range(N):
        if i == 0:
            max_gcd = gcd(A[i+1], A[i])
        elif i == N-1:
            max_gcd = max(max_gcd, gcd(A[i-1], A[i]))
        else:
            max_gcd = max(max_gcd, gcd(A[i-1], A[i+1]))
    print(max_gcd)

if __name__ == '__main__':
    main()