def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    A = []
    for i in range(N-K+1):
        A.append(max(P[i:i+K]))
    A.sort()
    for i in range(N-K+1):
        print(A[i])

if __name__ == '__main__':
    main()