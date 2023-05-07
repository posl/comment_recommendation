def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #B = A[0:M]
    B = A[0:M]
    #print(B)
    #print(sum(B))
    #print(sum(i * B[i] for i in range(len(B))))
    ans = sum(i * B[i] for i in range(len(B)))
    for i in range(1, N - M + 1):
        B = A[i:i + M]
        #print(B)
        #print(sum(B))
        #print(sum(i * B[i] for i in range(len(B))))
        ans = max(ans, sum(i * B[i] for i in range(len(B))))
    print(ans)

if __name__ == '__main__':
    main()