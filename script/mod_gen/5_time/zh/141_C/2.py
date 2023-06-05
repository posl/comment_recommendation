def main():
    N,K,Q = map(int,input().split())
    A = [int(input()) for i in range(Q)]
    #print(N,K,Q,A)
    ans = [0]*N
    for i in range(Q):
        ans[A[i]-1] += 1
    #print(ans)
    for i in range(N):
        if K+ans[i] - Q > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()