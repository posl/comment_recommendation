def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if M == 0:
            break
        if A[i] < 2 ** M:
            A[i] = 0
            M -= 1
        else:
            A[i] -= 2 ** M
            M = 0
    print(sum(A))

if __name__ == '__main__':
    main()