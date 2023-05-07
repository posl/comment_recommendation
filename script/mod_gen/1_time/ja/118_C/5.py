def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A))
        return
    A.sort()
    ans = A[0]
    for i in range(1,N):
        ans = gcd(ans, A[i])
    print(ans)

if __name__ == '__main__':
    main()