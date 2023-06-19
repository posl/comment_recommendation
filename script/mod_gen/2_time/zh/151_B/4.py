def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))
    score = sum(A)
    if score >= M*(N-1):
        print(M*N-score)
    else:
        print(-1)

if __name__ == '__main__':
    main()