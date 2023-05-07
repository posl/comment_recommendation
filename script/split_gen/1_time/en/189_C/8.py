def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        for j in range(i+1,N+1):
            for k in range(1,10**5+1):
                if min(A[i:j]) >= k:
                    ans = max(ans,k*(j-i))
    print(ans)
