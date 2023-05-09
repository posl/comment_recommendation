def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if M == N:
        print(0)
        return
    if M == 1:
        print(min(A[0], N - A[0] + 1))
        return
    diff = []
    for i in range(M - 1):
        diff.append(A[i + 1] - A[i] - 1)
    diff.sort()
    ans = N
    for i in range(M - 1):
        ans = min(ans, diff[i] + 1)
    print(ans)

if __name__ == '__main__':
    main()