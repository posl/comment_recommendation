def solve():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    B = [0 for i in range(N)]
    for i in range(N):
        B[A[i]-1] = i+1
    #print(B)
    ans = 0
    for i in range(N-1):
        if B[i] > B[i+1]:
            ans += 1
    print(ans+1)

if __name__ == '__main__':
    solve()