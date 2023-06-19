def main():
    n = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    K = [0] * (n + 1)
    for i in range(n):
        K[i + 1] = K[i] + (A[i] != A[i - 1]) # K[i]是A中小于A[i]的不同的整数的个数
    for i in range(1, n + 1):
        print(K[i])

if __name__ == '__main__':
    main()