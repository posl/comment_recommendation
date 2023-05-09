def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        for j in range(M):
            if i == A[j]-1 and H[i] <= H[B[j]-1]:
                break
            if i == B[j]-1 and H[i] <= H[A[j]-1]:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()