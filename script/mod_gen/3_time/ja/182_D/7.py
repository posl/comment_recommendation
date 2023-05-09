def main():
    N = int(input())
    A = list(map(int, input().split()))
    MAX = 0
    for i in range(N):
        MAX += max(A[i], 0)
    for i in range(N):
        if A[i] >= 0:
            print(MAX)
        else:
            print(MAX - max(A[i], 0) + max(A[i + 1:], 0))

if __name__ == '__main__':
    main()