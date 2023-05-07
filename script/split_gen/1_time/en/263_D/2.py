def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    
    A.sort()
    
    ans = 0
    for i in range(N):
        if i < N//2:
            ans += min(A[i], L)
        else:
            ans += min(A[i], R)
            
    print(ans)
