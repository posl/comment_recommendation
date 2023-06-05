def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(2*N+1)
    for i in range(N):
        B[A[i]] = i+1
    for i in range(1, 2*N+1):
        j = i
        while j > 0:
            print(i-j)
            j = B[j]//2

if __name__ == '__main__':
    solve()