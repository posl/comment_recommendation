def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        exit()
    if N == M:
        print(0)
        exit()
    B = []
    for i in range(M-1):
        B.append(A[i+1] - A[i] - 1)
    B.sort()
    B.reverse()
    if N == 1:
        print(0)
        exit()
    print(sum(B) + N - M - 1)

if __name__ == '__main__':
    main()