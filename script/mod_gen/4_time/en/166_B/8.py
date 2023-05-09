def main():
    # Get Input
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(int(input()))
    A = []
    for i in range(K):
        A.append([int(x) for x in input().split()])
    
    # Solve
    ans = 0
    for i in range(N):
        for j in range(K):
            if (i+1) in A[j]:
                break
            if j == K-1:
                ans += 1
    
    # Output
    print(ans)

if __name__ == '__main__':
    main()