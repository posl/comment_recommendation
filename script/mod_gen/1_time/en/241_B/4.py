def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(M):
        if B[i] > A[N-1]:
            print('No')
            return
        else:
            for j in range(N):
                if A[j] >= B[i]:
                    A[j] = 0
                    break
    print('Yes')
main()

if __name__ == '__main__':
    main()