def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    A = [0] + A + [N+1]
    d = []
    for i in range(M+1):
        if A[i+1] - A[i] > 1:
            d.append(A[i+1] - A[i] - 1)
    if len(d) == 0:
        print(0)
        return
    k = min(d)
    ans = 0
    for i in range(len(d)):
        ans += (d[i] + k - 1) // k
    print(ans)

if __name__ == '__main__':
    main()