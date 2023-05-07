def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append(abs(A[i] - B[i]))
    X = min(C)
    if X <= K:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()