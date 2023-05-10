def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(K):
        if B[i] > N:
            continue
        if A[0] == A[B[i]-1]:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()