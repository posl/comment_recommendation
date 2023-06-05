def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, P, Q, R)
    # print(A)
    # print(sum(A))
    # print(P+Q+R)
    if N == 3:
        if P+Q+R == sum(A):
            print('Yes')
        else:
            print('No')
    else:
        # print('No')
        # print(N, P, Q, R)
        # print(A)
        # print(sum(A))
        # print(P+Q+R)
        for i in range(N-3+1):
            for j in range(i+1, N-2+1):
                for k in range(j+1, N-1+1):
                    for l in range(k+1, N+1):
                        # print(i, j, k, l)
                        if sum(A[i:j]) == P and sum(A[j:k]) == Q and sum(A[k:l]) == R:
                            print('Yes')
                            return
        print('No')

if __name__ == '__main__':
    solve()