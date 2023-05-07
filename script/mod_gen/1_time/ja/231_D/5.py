def main():
    N, M = map(int, input().split())
    if M == 0:
        print('Yes')
        return
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    if N == 2 and M > 0:
        print('No')
        return
    if N == 3 and M > 1:
        print('No')
        return
    ans = 'Yes'
    for i in range(M):
        if A[i] == 1 and B[i] == N:
            ans = 'No'
            break
        if A[i] == 1 and B[i] == N-1:
            ans = 'No'
            break
        if A[i] == 2 and B[i] == N:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()