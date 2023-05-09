def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(gcd(A[0], A[1]))
        return
    A.sort()
    # print(A)
    # print(gcd(A[0], A[1]))
    # print(gcd(A[1], A[2]))
    # print(gcd(A[0], A[2]))
    print(max(gcd(A[0], A[1]), gcd(A[1], A[2]), gcd(A[0], A[2])))

if __name__ == '__main__':
    main()