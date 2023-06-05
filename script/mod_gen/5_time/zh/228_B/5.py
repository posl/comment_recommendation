def solve():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A = [i-1 for i in A]
    B = [0]*N
    B[X-1] = 1
    for i in range(N):
        if B[A[i]] == 1:
            B[i] = 1
    print(sum(B))

if __name__ == '__main__':
    solve()