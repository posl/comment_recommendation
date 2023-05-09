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
    diff = []
    for i in range(1, M):
        diff.append(A[i] - A[i-1] - 1)
    diff.sort()
    ans = 0
    for i in range(M - N + 1):
        ans += diff[i]
    print(ans + 1)
main()

if __name__ == '__main__':
    main()