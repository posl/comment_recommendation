def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (n + 1)
    for i in range(n + 1):
        B[i] = i
    for i in range(1, n + 1):
        for j in range(k):
            if i - A[j] >= 0:
                B[i] = min(B[i], B[i - A[j]] + 1)
    print(B[n])

if __name__ == '__main__':
    main()