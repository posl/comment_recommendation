def main():
    N,K,Q = map(int,input().split())
    A = list(map(int,input().split()))
    L = [int(input()) for i in range(Q)]
    ans = [0]*N
    for i in L:
        ans[i-1] += 1
    for i in range(N):
        if K - Q + ans[i] > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()