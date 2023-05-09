def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = float('inf')
    for i in range(1,N+1):
        ans = min(ans,abs(A[i-1]-i))
    print(ans)
