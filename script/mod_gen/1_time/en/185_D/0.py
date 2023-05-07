def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    A = [0] + A + [N + 1]
    B = []
    for i in range(M + 1):
        B.append(A[i + 1] - A[i] - 1)
    B.sort()
    B = B[::-1]
    k = B[0]
    for i in range(1, M + 1):
        k = gcd(k, B[i])
    print((B[0] + k - 1) // k)

if __name__ == '__main__':
    main()