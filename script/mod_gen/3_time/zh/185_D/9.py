def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    A = [0] + A + [N+1]
    # print(A)
    d = []
    for i in range(M+1):
        if A[i+1] - A[i] > 1:
            d.append(A[i+1] - A[i] - 1)
    # print(d)
    k = min(d)
    # print(k)
    ans = 0
    for i in d:
        ans += (i + k - 1) // k
    print(ans)

if __name__ == '__main__':
    main()