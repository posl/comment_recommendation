def sum_n(n):
    return n*(n+1)//2
N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
sum_A = sum(A)
sum_A2 = sum([a*a for a in A])
ans = 0
for i in range(N):
    sum_A -= A[i]
    sum_A2 -= A[i]*A[i]
    ans += A[i]*sum_A
    ans -= A[i]*A[i]*(N-1)
    ans -= A[i]*sum_n(N-1)
    ans += sum_A2
    ans %= mod
print(ans)

if __name__ == '__main__':
    sum_n()