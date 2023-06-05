def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if A[i] == K:
            count += 1
        for j in range(i+1,N):
            A[j] += A[j-1]
            if A[j] == K:
                count += 1
    print(count)

if __name__ == '__main__':
    main()