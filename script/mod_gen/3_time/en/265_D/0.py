def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                for l in range(k+1,N):
                    ans = max(ans, P*A[i]+Q*A[j]+R*A[k]+A[l])
    print(ans)

if __name__ == '__main__':
    main()