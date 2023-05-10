def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = [i for i in range(1,N+1)]
    for i in range(M):
        if ans[A[i]-1] > ans[B[i]-1]:
            ans[A[i]-1],ans[B[i]-1] = ans[B[i]-1],ans[A[i]-1]
    print(*ans)

if __name__ == '__main__':
    main()