def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    ans = 0
    for i in range(N):
        ans += min(B[i], A[i])
        A[i] -= min(B[i], A[i])
        ans += min(B[i], A[i+1])
        A[i+1] -= min(B[i], A[i+1])
    print(ans)
