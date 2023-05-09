def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    if N == K:
        print(1)
        return
    if K % 2 == 0:
        for i in range(N):
            if A[i] != i:
                break
        else:
            print(2)
            return
    print((N + K - 1) // K)
main()

if __name__ == '__main__':
    main()