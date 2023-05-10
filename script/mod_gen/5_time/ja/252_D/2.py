def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    res = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    res += 1
    print(res)
    return 0

if __name__ == '__main__':
    solve()