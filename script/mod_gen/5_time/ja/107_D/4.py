def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i]+A[i]
    print(B)
    print(B[N//2+1])
    print(B[N//2])
    print((B[N//2+1]+B[N//2])/2)
    if N%2==1:
        print(B[N//2+1])
    else:
        print((B[N//2+1]+B[N//2])/2)
    return 0

if __name__ == '__main__':
    solve()