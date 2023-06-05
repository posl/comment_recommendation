def main():
    N, Q = map(int, input().split())
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        A[i] = i - 1
        B[i] = i + 1
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[B[query[1]]] = A[query[1]]
            B[A[query[1]]] = B[query[1]]
            B[query[1]] = B[query[2]]
            A[B[query[2]]] = query[1]
            A[query[1]] = query[2]
            B[query[2]] = query[1]
        elif query[0] == 2:
            A[B[query[1]]] = A[query[1]]
            B[A[query[1]]] = B[query[1]]
            B[query[1]] = A[query[2]]
            A[B[query[2]]] = query[1]
            A[query[1]] = query[2]
            B[query[2]] = query[1]
        else:
            ans = []
            x = B[0]
            while x <= N:
                ans.append(x)
                x = B[x]
            print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()