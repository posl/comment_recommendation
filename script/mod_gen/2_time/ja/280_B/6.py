def main():
    N = int(input())
    S = list(map(int,input().split()))
    A = [0 for i in range(N)]
    A[0] = S[0]
    for i in range(1,N):
        A[i] = S[i] - A[i-1]
    print(' '.join(map(str,A)))

if __name__ == '__main__':
    main()