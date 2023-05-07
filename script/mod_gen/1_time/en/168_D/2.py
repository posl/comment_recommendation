def main():
    N, M = map(int, input().split())
    A, B = [], []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [0]*(N+1)
    ans[1] = 1
    for i in range(M):
        if ans[A[i]] != 0:
            ans[B[i]] = A[i]
        elif ans[B[i]] != 0:
            ans[A[i]] = B[i]
    if 0 in ans[2:]:
        print('No')
    else:
        print('Yes')
        for i in range(2, N+1):
            print(ans[i])

if __name__ == '__main__':
    main()