def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = [a-1 for a in A]
    B = [b-1 for b in B]
    C = [0]*N
    for i in range(M):
        if H[A[i]] == H[B[i]]:
            C[A[i]] += 1
            C[B[i]] += 1
        elif H[A[i]] > H[B[i]]:
            C[B[i]] += 1
        else:
            C[A[i]] += 1
    ans = 0
    for i in range(N):
        if C[i] == 0:
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()