def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(N+1)
    ans = 0
    for i in range(K):
        ans += A[i]*(A[i+1]-A[i]-1)
    print(ans)

if __name__ == '__main__':
    main()