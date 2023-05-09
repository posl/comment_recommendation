def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = N*(N-1)
    for i in range(M):
        for j in range(M):
            if A[i] == A[j] and B[i] == B[j]:
                ans -= 1
    print(ans)
main()

if __name__ == '__main__':
    main()