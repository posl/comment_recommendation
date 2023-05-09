def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A.sort()
    if A[0] == 0:
        print(0)
        return
    if N == 1:
        print(A[0])
        return
    ans = 0
    for i in range(N-1):
        ans += min(A[i], M-A[i])
    ans += min(A[-1], M-A[-1])
    print(ans)

if __name__ == '__main__':
    main()