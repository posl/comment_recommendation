def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    ans = 0
    for i in range(N):
        if A[i] < L:
            ans += L
        elif A[i] > R:
            ans += R
        else:
            ans += A[i]
    print(ans)
