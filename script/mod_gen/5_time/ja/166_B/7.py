def solve():
    N,K = map(int,input().split())
    d = [0]*K
    A = [0]*K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int,input().split()))
    cnt = 0
    for i in range(N):
        for j in range(K):
            if i+1 in A[j]:
                break
        else:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    solve()